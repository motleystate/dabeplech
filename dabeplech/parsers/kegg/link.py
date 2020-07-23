import logging
from collections import defaultdict

from dabeplech.models.kegg.link import KeggLinksModel
from dabeplech.parsers.base import BaseParser

logging.basicConfig()
logger = logging.getLogger()


class KeggLinkParser(BaseParser):
    """
    Parser for LINK operation from KEGG API.
    """
    model = KeggLinksModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parsed_content['links'] = defaultdict(lambda: list())

    def _parse_line(self, line):
        elements = line.split()
        key_id = elements[0].split(':')[1]
        linked_id = elements[1].split(':')[1]
        self.parsed_content['links'][key_id].append(linked_id)

    def parse(self):
        for line in self.lines:
            self._parse_line(line)
