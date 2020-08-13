from bs4 import BeautifulSoup

from dabeplech.models.ncbi_taxonomy.taxonomy import NCBITaxonomyAPIModel


class NCBITaxonomyScrapper:
    """
    Scrapper of html response from NCBI taxonomy info page of a given tax_id
    """
    model = NCBITaxonomyAPIModel

    def __init__(self, html_content: bytes):
        self.soup = BeautifulSoup(html_content, features="html.parser")

    def result_found(self):
        """
        if <h1> is present in the page, it means an error message is returned
        """
        if self.soup.h1 is not None:
            return False
        return True

    @classmethod
    def extract_tax_id_from_url(self, url):
        qparams = url.split('?', maxsplit=1)[1]
        for qparam in qparams.split('&'):
            if 'id=' in qparam:
                return qparam.split('=')[-1]

    def retrieve_current_item(self):
        table_of_interest = self.soup.body.find_all('table')[3]
        name = table_of_interest.find_all('strong')[0].text
        tax_id = table_of_interest.tr.td.text.split("Taxonomy ID:", maxsplit=1)[-1].split()[0]
        rank = table_of_interest.find_all('strong')[-2].text
        current_item = {
            'rank': rank,
            'tax_id': tax_id,
            'name': name
        }
        return current_item

    def retrieve_hierarchy(self):
        hierarchy = []
        for i in self.soup.dd.find_all('a'):
            hierarchy.append({
                'rank': i['title'],
                'tax_id': self.extract_tax_id_from_url(i['href']),
                'name': i.text
            })
        return hierarchy

    def scrap(self):
        """
        Perform scrapping of the content of interest
        """
        self.entry = {}
        self.entry['current_item'] = self.retrieve_current_item()
        self.entry['hierarchy'] = self.retrieve_hierarchy()

    @property
    def validated_entry(self):
        """
        :return: Validated entry in the model described in dabeplech.
        :rtype: dict
        """
        if getattr(self, 'entry', None) is None:
            self.scrap()
        return self.model(**self.entry)
