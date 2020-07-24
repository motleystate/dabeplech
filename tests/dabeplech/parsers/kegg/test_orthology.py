import os
from unittest import TestCase

from dabeplech.parsers.kegg import KeggOrthologyParser, KeggOrthologyListParser


class TestKeggOrthologyParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/K00135.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggOrthologyParser(test_txt)
        test_parser.parse()
        tested_entry = test_parser.validated_entry
        # Test some of the attribute and content of the file
        self.assertEqual(tested_entry.entry_id, 'K00135')
        self.assertIn('gabD', tested_entry.names)
        self.assertEqual(tested_entry.definition, 'succinate-semialdehyde dehydrogenase / glutarate-semialdehyde dehydrogenase')  # noqa
        # Test ec numbers list
        self.assertEqual(len(tested_entry.ec_numbers), 3)
        for ec_number in ['1.2.1.16', '1.2.1.79', '1.2.1.20']:
            self.assertIn(ec_number, tested_entry.ec_numbers)
        # Test some keys of dictionnary
        self.assertIn('ko00250', tested_entry.pathways.keys())
        self.assertIn('Alanine, aspartate and glutamate metabolism', tested_entry.pathways.values())
        self.assertIn('M00027', tested_entry.modules.keys())
        self.assertIn('RN', tested_entry.dblinks.dict().keys())
        self.assertIn('LVE', tested_entry.genes.keys())
        # Test references
        self.assertEqual(len(tested_entry.references), 2)
        self.assertEqual(tested_entry.references[0].pubmed_id, 2254272)
        self.assertEqual(tested_entry.references[0].doi, "10.1128/JB.172.12.7035-7042.1990")


class TestKeggOrthologyListParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/list_ko.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggOrthologyListParser(test_txt)
        test_parser.parse()
        tested_model = test_parser.validated_model
        self.assertEqual(len(tested_model.entries), 10)
        # Testing third entry of the list
        tested_entry = tested_model.entries[2]
        self.assertEqual(tested_entry.entry_id, 'K00003')
        self.assertIn('hom', tested_entry.names)
        self.assertEqual(tested_entry.definition, 'homoserine dehydrogenase')
        # Test entry has only expected
        for k in vars(tested_entry).keys():
            self.assertIn(k, ['names', 'entry_id', 'definition', 'ec_numbers'])

    def test_empty_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/empty_list.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggOrthologyListParser(test_txt)
        test_parser.parse()
        tested_model = test_parser.validated_model
        self.assertEqual(len(tested_model.entries), 0)
