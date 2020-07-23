import os
from unittest import TestCase

from dabeplech.parsers.kegg.link import KeggLinkParser


class TestKeggLinkParser(TestCase):

    def test_parsing(self):
        input_path = os.path.join(os.path.dirname(__file__), 'files/link_pathway_K00135.txt')
        test_file = open(input_path, 'r')
        test_txt = test_file.read()
        test_parser = KeggLinkParser(test_txt)
        test_parser.parse()
        tested_entry = test_parser.validated_entry
        # Test some of the attribute and content of the file
        self.assertEqual(len(tested_entry.links), 1)
        for entry_id, entries_list in tested_entry.links.items():
            self.assertEqual(entry_id, 'K00135')
            self.assertEqual(len(entries_list), 14)
            self.assertIn('ko01100', entries_list)
