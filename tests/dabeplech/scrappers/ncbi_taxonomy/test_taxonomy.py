import os
from unittest import TestCase

from dabeplech.scrappers.ncbi_taxonomy.taxonomy import NCBITaxonomyScrapper


class TestNCBITaxonomyScrapper(TestCase):

    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__), 'data/tax_33958.html')
        self.file = open(file_path, "rb")

    def test_result_found(self):
        scrapper = NCBITaxonomyScrapper(self.file)
        self.assertTrue(scrapper.result_found())

    def test_result_found_error_page(self):
        file_path = os.path.join(os.path.dirname(__file__), 'data/error_page.html')
        tax_file = open(file_path, "rb")
        scrapper = NCBITaxonomyScrapper(tax_file)
        self.assertFalse(scrapper.result_found())

    def test_extract_tax_id_from_url(self):
        tested_url = "wwwtax.cgi?mode=Undef&amp;id=131567&amp;lvl=3&amp;keep=1&amp;srchmode=1&amp;unlock"
        expected_id = "131567"
        tested_id = NCBITaxonomyScrapper.extract_tax_id_from_url(tested_url)
        self.assertEqual(tested_id, expected_id)

    def test_retrieve_current_item(self):
        scrapper = NCBITaxonomyScrapper(self.file)
        expected_dict = {
            'rank': 'family',
            'tax_id': '33958',
            'name': 'Lactobacillaceae'
        }
        tested_dict = scrapper.retrieve_current_item()
        self.assertDictEqual(tested_dict, expected_dict)

    def test_retrieve_current_item_no_link(self):
        """
        Some entry has their names without a link, for instance tax_id 339588
        """
        file_path = os.path.join(os.path.dirname(__file__), 'data/tax_339588.html')
        tax_file = open(file_path, "rb")
        scrapper = NCBITaxonomyScrapper(tax_file)
        expected_dict = {
            'rank': 'species',
            'tax_id': '339588',
            'name': 'Peyssonnelia inamoena'
        }
        tested_dict = scrapper.retrieve_current_item()
        self.assertDictEqual(tested_dict, expected_dict)

    def test_retrieve_current_item_variant_1(self):
        """
        Some entry has different display and more information, for instance tax_id 12345
        """
        file_path = os.path.join(os.path.dirname(__file__), 'data/tax_12345.html')
        tax_file = open(file_path, "rb")
        scrapper = NCBITaxonomyScrapper(tax_file)
        expected_dict = {
            'rank': 'species',
            'tax_id': '12345',
            'name': 'Bacillus virus GA1'
        }
        tested_dict = scrapper.retrieve_current_item()
        self.assertDictEqual(tested_dict, expected_dict)

    def test_retrieve_hierarchy(self):
        scrapper = NCBITaxonomyScrapper(self.file)
        expected_list = [
            {'name': 'cellular organisms', 'rank': 'no rank', 'tax_id': '131567'},
            {'name': 'Bacteria', 'rank': 'superkingdom', 'tax_id': '2'},
            {'name': 'Terrabacteria group', 'rank': 'clade', 'tax_id': '1783272'},
            {'name': 'Firmicutes', 'rank': 'phylum', 'tax_id': '1239'},
            {'name': 'Bacilli', 'rank': 'class', 'tax_id': '91061'},
            {'name': 'Lactobacillales', 'rank': 'order', 'tax_id': '186826'}
        ]
        tested_list = scrapper.retrieve_hierarchy()
        self.assertListEqual(tested_list, expected_list)
