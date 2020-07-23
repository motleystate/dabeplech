import logging

from dabeplech.models.kegg import KeggOrthologyModel
from dabeplech.parsers.kegg.base import BaseKeggParser

logging.basicConfig()
logger = logging.getLogger()


class KeggOrthologyParser(BaseKeggParser):
    """
    Parser for KEGG KO `plain text` result from KEGG API.
    """
    model = KeggOrthologyModel

    def _handle_definition(self, line: str, **kwargs):
        def_and_ec_numbers = line.split(maxsplit=1)[-1]
        if 'EC:' in def_and_ec_numbers:
            elements = def_and_ec_numbers.split('[')
            self.entry.definition = elements[0].strip()
            self.entry.ec_numbers = elements[1].replace(']', '').replace('EC:', '').strip().split()
        else:
            self.entry.definition = def_and_ec_numbers
