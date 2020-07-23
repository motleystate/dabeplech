import logging

from dabeplech.models.kegg.module import KeggModuleModel
from dabeplech.parsers.kegg.base import BaseKeggParser

logging.basicConfig()
logger = logging.getLogger()


class KeggModuleParser(BaseKeggParser):
    """
    Parser for KEGG module `plain text` result from KEGG API.
    """
    model = KeggModuleModel
