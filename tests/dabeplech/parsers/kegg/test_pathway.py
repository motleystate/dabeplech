import os
from unittest import TestCase

from dabeplech.parsers.kegg.list import KeggPathwayListParser
from dabeplech.parsers.kegg.pathway import KeggPathwayParser


class TestKeggPathwayParser(TestCase):

    def _get_tested_entry(self, file_path):
        input_path = os.path.join(os.path.dirname(__file__), file_path)
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggPathwayParser(test_txt)
        test_parser.parse()
        return test_parser.validated_entry

    def _common_tests(self, tested_entry):
        # Test some of the attribute and content of the file
        self.assertIn('Tyrosine metabolism', tested_entry.names)
        # Test some keys of dictionnary
        self.assertIn('M00042', tested_entry.modules.keys())
        self.assertIn('GO', tested_entry.dblinks.dict().keys())
        self.assertIn('H00163', tested_entry.diseases.keys())
        # Test references
        self.assertEqual(len(tested_entry.references), 4)
        self.assertEqual(tested_entry.references[0].pubmed_id, 8550403)
        self.assertEqual(tested_entry.references[0].doi, "10.1128/JB.178.1.111-120.1996")

    def test_parsing_ko(self):
        tested_entry = self._get_tested_entry('files/ko00350.txt')
        self._common_tests(tested_entry)
        # Test specifics
        self.assertEqual(tested_entry.entry_id, 'ko00350')
        # Keys of dict
        self.assertIn('ko00020', tested_entry.related_pathways.keys())
        self.assertIn('C00022', tested_entry.compounds.keys())
        self.assertIn('K14454', tested_entry.orthologies.keys())
        self.assertIn('ko00350', tested_entry.pathway_maps.keys())

    def test_parsing_map(self):
        tested_entry = self._get_tested_entry('files/map00350.txt')
        self._common_tests(tested_entry)
        # Test specifics
        self.assertEqual(tested_entry.entry_id, 'map00350')
        self.assertEqual(tested_entry.ko_pathway, 'ko00350')
        # List
        self.assertIn('Amino acid metabolism', tested_entry.classes)
        # Keys of dict
        self.assertIn('map00020', tested_entry.related_pathways.keys())
        self.assertIn('map00350', tested_entry.pathway_maps.keys())

    def test_parsing_map_with_ref_no_pubmedid(self):
        tested_entry = self._get_tested_entry('files/map00030.txt')
        # Test some of the attribute and content of the file
        self.assertIn('Pentose phosphate pathway', tested_entry.names)
        # Test some keys of dictionnary
        self.assertIn('M00004', tested_entry.modules.keys())
        self.assertIn('GO', tested_entry.dblinks.dict().keys())
        self.assertIn('H00196', tested_entry.diseases.keys())
        # Test references
        self.assertEqual(len(tested_entry.references), 9)
        self.assertEqual(tested_entry.references[0].title, "[Metabolic Maps] (In Japanese)")
        # Test specifics
        self.assertEqual(tested_entry.entry_id, 'map00030')
        self.assertEqual(tested_entry.ko_pathway, 'ko00030')
        # List
        self.assertIn('Metabolism', tested_entry.classes)
        # Keys of dict
        self.assertIn('map00052', tested_entry.related_pathways.keys())
        self.assertIn('map00030', tested_entry.pathway_maps.keys())


class TestKeggPathwayListParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/list_pathway.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggPathwayListParser(test_txt)
        test_parser.parse()
        tested_model = test_parser.validated_model
        self.assertEqual(len(tested_model.entries), 10)
        # Testing third entry of the list
        tested_entry = tested_model.entries[2]
        self.assertEqual(tested_entry.entry_id, 'map00030')
        self.assertIn('Pentose phosphate pathway', tested_entry.names)
        # Test entry has only expected
        for k in vars(tested_entry).keys():
            self.assertIn(k, ['names', 'entry_id'])
