import logging

from dabeplech.models.kegg import KeggPathwayModel
from dabeplech.parsers.kegg.base import BaseKeggParser

logging.basicConfig()
logger = logging.getLogger()


class KeggPathwayKoParser(BaseKeggParser):
    model = KeggPathwayModel


class KeggPathwayMapParser(BaseKeggParser):
    model = KeggPathwayModel

    def _handle_ko_pathway(self, line, **kwargs):
        self.entry.ko_pathway = line.split(maxsplit=1)[-1].strip()


class KeggPathwayParser(KeggPathwayKoParser, KeggPathwayMapParser):
    """
    Parser for KEGG KO `plain text` result from KEGG API.
    """
    model = KeggPathwayModel

    def _handle_pathway_map(self, line, first=False):
        self._simple_handling(line, 'pathway_maps', first=first)

    def _handle_rel_pathway(self, line, first=False):
        self._simple_handling(line, 'related_pathways', first=first)
