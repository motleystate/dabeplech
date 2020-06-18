import os
from unittest import TestCase

from bioapi.parsers.kegg import KeggOrthologyParser


class TestKeggOrthologyParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/example_K00135.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggOrthologyParser(test_txt)
        test_parser.parse()
        tested_entry = test_parser.validated_entry
        # Test some of the attribute and content of the file
        self.assertEqual(tested_entry.entry_id, 'K00135')
        self.assertEqual(tested_entry.name, 'gabD')
        self.assertEqual(tested_entry.definition, 'succinate-semialdehyde dehydrogenase / glutarate-semialdehyde dehydrogenase')  # noqa
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
