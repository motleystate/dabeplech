import logging

from bioapi.models.kegg import KeggPathwayModel
from bioapi.parsers.kegg.base import BaseKeggParser

logging.basicConfig()
logger = logging.getLogger()


class KeggPathwayKoParser(BaseKeggParser):
    model = KeggPathwayModel

    def _handle_orthology(self, line, first=False):
        self._simple_handling(line, 'orthologs', first=first)

    def _handle_compound(self, line, first=False):
        self._simple_handling(line, 'compounds', first=first)


class KeggPathwayMapParser(BaseKeggParser):
    model = KeggPathwayModel

    def _handle_ko_pathway(self, line, **kwargs):
        self.entry.ko_pathway = line.split(maxsplit=1)[-1].strip()


class KeggPathwayParser(KeggPathwayKoParser, KeggPathwayMapParser):
    """
    Parser for KEGG KO `plain text` result from KEGG API.
    """
    model = KeggPathwayModel

    def _handle_description(self, line: str, **kwargs):
        self.entry.description = line.split(maxsplit=1)[-1]

    def _handle_class(self, line, first=False):
        if first:
            self.entry.classes = []
        classes = [element.strip() for element in line.split(maxsplit=1)[-1].split(';')]
        self.entry.classes = self.entry.classes + classes

    def _handle_pathway_map(self, line, first=False):
        self._simple_handling(line, 'pathway_maps', first=first)

    def _handle_rel_pathway(self, line, first=False):
        self._simple_handling(line, 'related_pathways', first=first)
