from bs4 import BeautifulSoup

from dabeplech.models.ncbi_taxonomy.taxonomy import NCBITaxonomyAPIModel


class NCBITaxonomyScrapper:
    """
    Scrapper of html response from NCBI taxonomy info page of a given tax_id
    """

    def __init__(self, html_content: bytes):
        self.soup = BeautifulSoup(html_content, features="html.parser")

    @classmethod
    def extract_tax_id_from_url(self, url):
        qparams = url.split('?', maxsplit=1)[1]
        for qparam in qparams.split('&'):
            if 'id=' in qparam:
                return qparam.split('=')[-1]

    def retrieve_current_item(self):
        table_of_interest = self.soup.body.find_all('table')[3]
        name = table_of_interest.a.text
        tax_id = self.extract_tax_id_from_url(table_of_interest.a['href'])
        rank = table_of_interest.find_all('strong')[2].text
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
        return NCBITaxonomyAPIModel(**self.entry)
