import logging

from dabeplech.models.kegg.base import BaseKeggModel
from dabeplech.parsers.base import BaseParser
from dabeplech.parsers.kegg.reference import KeggReferenceParser

logging.basicConfig()
logger = logging.getLogger()


class BaseKeggParser(BaseParser):
    """
    Base structure for parsers for KEGG API
    """
    model = BaseKeggModel  # Pydantic model to describe the response

    def __init__(self, content_response: str):
        """
        :param content_response: content response from the API
        """
        self.lines = content_response.rstrip().split('\n')
        self.handler = '_handle_entry'
        self.current_ref = None
        self.skipped_lines = 0

    def _simple_handling(self, line: str, attr_to_set: str, first: bool = False):
        if first:
            elements = line.split(maxsplit=2)
            if len(elements) > 2:
                value = elements[2]
            else:
                value = None
            setattr(self.entry, attr_to_set, {elements[1]: value})
        else:
            elements = line.split(maxsplit=1)
            if len(elements) > 1:
                value = elements[1]
            else:
                value = None
            getattr(self.entry, attr_to_set)[elements[0]] = value

    def _simple_handling_list(self, line: str, attr_to_set: str, first=False):
        if first:
            elements = line.split(maxsplit=2)
            setattr(self.entry, attr_to_set, {elements[1].rstrip(':'): elements[2].split()})
        else:
            elements = line.split(maxsplit=1)
            getattr(self.entry, attr_to_set)[elements[0].rstrip(':')] = elements[1].split()

    def _handle_default(self, line: str, **kwargs):
        logger.info("Skipped line: %s" % line)
        self.skipped_lines += 1

    def _handle_entry(self, line: str, **kwargs):
        entry_id = line.split()[1]
        # Starts a Kegg Orthology object with name that will be updated
        self.entry = self.model(entry_id=entry_id, names=[])

    def _handle_definition(self, line: str, first: bool = False):
        self.entry.definition = line.split(maxsplit=1)[-1]

    def _handle_pathway(self, line: str, first: bool = False):
        self._simple_handling(line, 'pathways', first=first)

    def _handle_brite(self, line: str, **kwargs):
        logger.info("Skipping BRITE part of the response...")
        pass

    def _handle_genes(self, line: str, first: bool = False):
        self._simple_handling_list(line, 'genes', first=first)

    def _handle_name(self, line: str, **kwargs):
        names = line.split(maxsplit=1)[-1].split(",")
        self.entry.names = [name.strip() for name in names]

    def _handle_dblinks(self, line: str, first: bool = False):
        self._simple_handling_list(line, 'dblinks', first=first)

    def _handle_module(self, line: str, first: bool = False):
        self._simple_handling(line, 'modules', first=first)

    def _handle_disease(self, line: str, first: bool = False):
        self._simple_handling(line, 'diseases', first=first)

    def _handle_orthology(self, line: str, first: bool = False):
        self._simple_handling(line, 'orthologies', first=first)

    def _handle_compound(self, line: str, first: bool = False):
        self._simple_handling(line, 'compounds', first=first)

    def _handle_rmodule(self, line: str, first: bool = False):
        self._simple_handling(line, 'rmodules', first=first)

    def _handle_reaction(self, line, first=False):
        if not line.strip():
            return
        if first:
            elements = line.split(maxsplit=2)
            reaction_ids_str = elements[1]
        else:
            elements = line.split(maxsplit=1)
            reaction_ids_str = elements[0]
        reaction_ids = reaction_ids_str.split(',')
        reaction = elements[-1]
        for reaction_id in reaction_ids:
            if getattr(self.entry, 'reactions') is None:
                setattr(self.entry, 'reactions', {reaction_id: reaction})
            else:
                getattr(self.entry, 'reactions')[reaction_id] = reaction

    def _handle_description(self, line: str, **kwargs):
        self.entry.description = line.split(maxsplit=1)[-1]

    def _handle_class(self, line: str, first: bool = False):
        if first:
            self.entry.classes = []
        classes = [element.strip() for element in line.split(maxsplit=1)[-1].split(';')]
        self.entry.classes = self.entry.classes + classes

    def _handle_comment(self, line: str, **kwargs):
        self.entry.comment = line.split(maxsplit=1)[-1].strip()

    def _handle_reference_first(self, line: str):
        if self.current_ref is not None:
            self.entry.references.append(self.current_ref.dict())
        else:  # First time we encounter reference and there will be at least one
            self.entry.references = []
        self.current_ref = KeggReferenceParser()
        self.current_ref.pubmed_id = line

    def _handle_reference_other(self, line: str):
        elements = line.split(maxsplit=1)
        if len(elements) > 1:
            attribute = elements[0].lower()
        else:  # case of handling doi
            attribute = line.strip().split(':')[0].lower()
        setattr(self.current_ref, attribute, line)

    def _handle_reference(self, line: str, first: bool = False):
        if first is True:
            self._handle_reference_first(line)
        else:
            self._handle_reference_other(line)

    def _reattach_last_elements(self):
        """
        This aims to deal with last elements (like in references) that are not appended to their list
        """
        if self.current_ref is not None:
            self.entry.references.append(self.current_ref.dict())

    def parse(self):
        """
        Perform parsing of the text content into the model defined for KEGG orthology.
        """
        for line in self.lines:
            if '///' in line:  # end of lines
                break
            if not line.startswith(' '):  # There is a category to be handled
                category = line.split()[0].lower()
                handler = f"_handle_{category}"
                getattr(self, handler, self._handle_default)(line, first=True)
            else:
                getattr(self, handler, self._handle_default)(line)
        self._reattach_last_elements()

    @property
    def validated_entry(self):
        """
        :return: Validated entry for KEGG orthology.
        :rtype: dict
        """
        # Reparse all the content of entry to make sure it respects the expected structure
        if self.skipped_lines > 0:
            logger.warning("%s lines skipped from parsing for %s", self.skipped_lines, self.entry.entry_id)
        return self.model(**self.entry.dict())
