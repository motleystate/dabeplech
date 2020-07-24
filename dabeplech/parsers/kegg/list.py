import logging

from dabeplech.models.kegg.orthology import KeggOrthologyListModel
from dabeplech.models.kegg.pathway import KeggPathwayListModel
from dabeplech.parsers.base import BaseListParser

logging.basicConfig()
logger = logging.getLogger()


class BaseKeggListParser(BaseListParser):

    def _parse_line(self, line):
        elements = line.split(maxsplit=1)
        entry_id = elements[0].split(':')[1]
        names = elements[1].split(';')[0].split(',')
        names = [name.strip() for name in names]
        return {
            'entry_id': entry_id,
            'names': names,
        }

    def parse(self):
        for line in self.lines:
            if not line.strip():
                continue
            self.parsed_content.append(self._parse_line(line))


class KeggOrthologyListParser(BaseKeggListParser):
    """
    Parser for list of KEGG ko from KEGG API (http://rest.kegg.jp/list/ko).
    """
    model = KeggOrthologyListModel

    def _parse_line(self, line):
        elements = line.split(maxsplit=1)
        entry_id = elements[0].split(':')[1]
        names = elements[1].split(';')[0].split(',')
        names = [name.strip() for name in names]
        if ';' in elements[1]:
            definition = elements[1].split(';')[1].split('[')[0].strip()
        else:
            definition = None
        if '[' in elements[1]:
            ec_numbers = elements[1].split('[')[1].rstrip(']').replace('EC:', '').split()
        else:
            ec_numbers = None
        return {
            'entry_id': entry_id,
            'names': names,
            'definition': definition,
            'ec_numbers': ec_numbers
        }


class KeggPathwayListParser(BaseKeggListParser):
    """
    Parser for list of KEGG pathways (map) from KEGG API (http://rest.kegg.jp/list/pathway).
    """
    model = KeggPathwayListModel


class KeggModuleListParser(BaseKeggListParser):
    """
    Parser for list of KEGG modules (M) from KEGG API (http://rest.kegg.jp/list/module).
    """
    model = KeggPathwayListModel
