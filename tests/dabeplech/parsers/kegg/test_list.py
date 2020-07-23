from unittest import TestCase

from dabeplech.parsers.kegg.list import KeggOrthologyListParser, KeggPathwayListParser


class TestKeggOrthologyList(TestCase):

    def test_parse_line(self):
        line = "ko:K00001	E1.1.1.1, adh; alcohol dehydrogenase [EC:1.1.1.1]"
        expected_dict = {
            'entry_id': 'K00001',
            'names': ['E1.1.1.1', 'adh'],
            'definition': 'alcohol dehydrogenase',
            'ec_numbers': ['1.1.1.1']
        }
        parser = KeggOrthologyListParser("test")
        self.assertDictEqual(parser._parse_line(line), expected_dict)

    def test_parse_line_multi_ec_numbers(self):
        line = "ko:K00010	iolG; myo-inositol 2-dehydrogenase / D-chiro-inositol 1-dehydrogenase [EC:1.1.1.18 1.1.1.369]"  # noqa
        expected_dict = {
            'entry_id': 'K00010',
            'names': ['iolG'],
            'definition': 'myo-inositol 2-dehydrogenase / D-chiro-inositol 1-dehydrogenase',
            'ec_numbers': ['1.1.1.18', '1.1.1.369']
        }
        parser = KeggOrthologyListParser("test")
        self.assertDictEqual(parser._parse_line(line), expected_dict)

    def test_parse_line_no_ec_numbers(self):
        line = "ko:K00182	WNT2; wingless-type MMTV integration site family, member 2"
        expected_dict = {
            'entry_id': 'K00182',
            'names': ['WNT2'],
            'definition': 'wingless-type MMTV integration site family, member 2',
            'ec_numbers': None
        }
        parser = KeggOrthologyListParser("test")
        self.assertDictEqual(parser._parse_line(line), expected_dict)

    def test_parse_line_no_definition_no_ec_numbers(self):
        line = "ko:K23479       CCAAT/enhancer binding protein (C/EBP), other"
        expected_dict = {
            'entry_id': 'K23479',
            'names': ['CCAAT/enhancer binding protein (C/EBP)', 'other'],
            'definition': None,
            'ec_numbers': None
        }
        parser = KeggOrthologyListParser("test")
        self.assertDictEqual(parser._parse_line(line), expected_dict)


class TestKeggPathwayList(TestCase):

    def test_parse_line(self):
        line = "path:map00030	Pentose phosphate pathway"
        expected_dict = {
            'entry_id': 'map00030',
            'names': ['Pentose phosphate pathway'],
        }
        parser = KeggPathwayListParser("test")
        self.assertDictEqual(parser._parse_line(line), expected_dict)
