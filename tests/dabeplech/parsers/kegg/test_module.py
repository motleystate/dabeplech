import os
from unittest import TestCase

from dabeplech.parsers.kegg.module import KeggModuleParser
from dabeplech.parsers.kegg.list import KeggModuleListParser


class TestKeggModuleParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/M00003.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggModuleParser(test_txt)
        test_parser.parse()
        tested_entry = test_parser.validated_entry
        # Test some of the attribute and content of the file
        self.assertEqual(tested_entry.entry_id, 'M00003')
        self.assertEqual(tested_entry.definition, "(K01596,K01610) K01689 (K01834,K15633,K15634,K15635) K00927 (K00134,K00150) K01803 ((K01623,K01624,K11645) (K03841,K02446,K11532,K01086,K04041),K01622)")  # noqa
        self.assertIn('Gluconeogenesis', tested_entry.names)
        # Test some keys of dictionnary
        self.assertIn('map00020', tested_entry.pathways.keys())
        self.assertIn('Glycolysis / Gluconeogenesis', tested_entry.pathways.values())
        self.assertIn('R01518', tested_entry.reactions.keys())
        self.assertIn('R00726', tested_entry.reactions.keys())
        self.assertIn('C00111', tested_entry.compounds.keys())

    def test_parsing_empty_lines(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/M00083.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggModuleParser(test_txt)
        test_parser.parse()
        tested_entry = test_parser.validated_entry
        # Test some of the attribute and content of the file
        self.assertEqual(tested_entry.entry_id, 'M00083')
        self.assertIn('Fatty acid biosynthesis', tested_entry.names)
        # Test some keys of dictionnary
        self.assertIn('R04959', tested_entry.reactions.keys())


class TestKeggModuleListParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/list_module.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggModuleListParser(test_txt)
        test_parser.parse()
        tested_model = test_parser.validated_model
        self.assertEqual(len(tested_model.entries), 10)
        # Testing third entry of the list
        tested_entry = tested_model.entries[2]
        self.assertEqual(tested_entry.entry_id, 'M00003')
        self.assertIn('Gluconeogenesis', tested_entry.names)
        # Test entry has only expected
        for k in vars(tested_entry).keys():
            self.assertIn(k, ['names', 'entry_id'])
