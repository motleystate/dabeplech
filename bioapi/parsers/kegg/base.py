import logging

from bioapi.models.kegg.base import BaseKeggModel
from bioapi.parsers.kegg.reference import KeggReferenceParser

logging.basicConfig()
logger = logging.getLogger()


class BaseKeggParser:
    """
    Base structure for parsers for KEGG API
    """
    model = BaseKeggModel  # Pydantic model to describe the response

    def __init__(self, text_response: str):
        """
        :param text_response: Full plain text response from KEGG API
        """
        self.lines = text_response.rstrip().split('\n')
        self.handler = '_handle_entry'
        self.current_ref = None
        self.skipped_lines = 0

    def _handle_default(self, line: str, **kwargs):
        logger.info("Skipped line: %s" % line)
        self.skipped_lines += 1

    def _handle_entry(self, line: str, **kwargs):
        entry_id = line.split()[1]
        # Starts a Kegg Orthology object with name that will be updated
        self.entry = self.model(entry_id=entry_id, name=entry_id)

    def _handle_name(self, line: str, **kwargs):
        self.entry.name = line.split(maxsplit=1)[-1]

    def _simple_handling(self, line: str, attr_to_set: str, first: bool = False):
        if first:
            elements = line.split(maxsplit=2)
            setattr(self.entry, attr_to_set, {elements[1]: elements[2]})
        else:
            elements = line.split(maxsplit=1)
            getattr(self.entry, attr_to_set)[elements[0]] = elements[1]

    def _simple_handling_list(self, line, attr_to_set, first=False):
        if first:
            elements = line.split(maxsplit=2)
            setattr(self.entry, attr_to_set, {elements[1].rstrip(':'): elements[2].split()})
        else:
            elements = line.split(maxsplit=1)
            getattr(self.entry, attr_to_set)[elements[0].rstrip(':')] = elements[1].split()

    def _handle_dblinks(self, line, first=False):
        self._simple_handling_list(line, 'dblinks', first=first)

    def _handle_module(self, line, first=False):
        self._simple_handling(line, 'modules', first=first)

    def _handle_reference_first(self, line):
        if self.current_ref is not None:
            self.entry.references.append(self.current_ref.dict())
        else:  # First time we encounter reference and there will be at least one
            self.entry.references = []
        self.current_ref = KeggReferenceParser()
        self.current_ref.pubmed_id = line

    def _handle_reference_other(self, line):
        elements = line.split(maxsplit=1)
        if len(elements) > 1:
            attribute = elements[0].lower()
        else:  # case of handling doi
            attribute = line.strip().split(':')[0].lower()
        setattr(self.current_ref, attribute, line)

    def _handle_reference(self, line, first=False):
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
            logger.warning("%s lines skipped from parsing")
        return self.model(**self.entry.dict())
