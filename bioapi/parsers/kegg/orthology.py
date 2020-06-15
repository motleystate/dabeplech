import logging

from bioapi.models.kegg import KeggOrthologyModel
from bioapi.parsers.kegg.reference import KeggReferenceParser

logging.basicConfig()
logger = logging.getLogger()


class KeggOrthologyParser:

    def __init__(self, text_response):
        self.lines = text_response.rstrip().split('\n')
        self.handler = '_handle_entry'
        self.current_ref = None
        self.skipped_lines = 0

    def _handle_default(self, line, **kwargs):
        # logging.warning("not implemented yet")
        self.skipped_lines += 1

    def _handle_entry(self, line, **kwargs):
        entry_id = line.split()[1]
        # Starts a Kegg Orthology object with name that will be updated
        self.entry = KeggOrthologyModel(entry_id=entry_id, name=entry_id)

    def _handle_name(self, line, **kwargs):
        self.entry.name = line.split()[1]

    def _handle_definition(self, line, **kwargs):
        def_and_ec_numbers = line.split(maxsplit=1)[-1]
        if 'EC' in def_and_ec_numbers:
            elements = def_and_ec_numbers.split('[')
            self.entry.definition = elements[0].strip()
            self.entry.ec_numbers = elements[1].replace(']', '').replace('EC:', '').strip().split()
        else:
            self.entry.definition = def_and_ec_numbers

    def _simple_handling(self, line, attr_to_set, first=False):
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

    def _handle_pathway(self, line, first=False):
        self._simple_handling(line, 'pathways', first=first)

    def _handle_module(self, line, first=False):
        self._simple_handling(line, 'modules', first=first)

    def _handle_brite(self, line, **kwargs):
        # not handling brite, might type warning here
        pass

    def _handle_dblinks(self, line, first=False):
        self._simple_handling_list(line, 'dblinks', first=first)

    def _handle_genes(self, line, first=False):
        self._simple_handling_list(line, 'genes', first=first)

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
        for line in self.lines:
            if not line.startswith(' '):  # There is a category to be handled
                category = line.split()[0].lower()
                handler = f"_handle_{category}"
                getattr(self, handler, self._handle_default)(line, first=True)
            else:
                getattr(self, handler, self._handle_default)(line)
        self._reattach_last_elements()

    @property
    def validated_entry(self):
        # Reparse all the content of entry to make sure it respects the expected structure
        return KeggOrthologyModel(**self.entry.dict())
