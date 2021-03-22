"""Scrappers for NCBI Taxonomy."""
from bs4 import BeautifulSoup

from dabeplech.models.ncbi_taxonomy import NCBITaxonomyAPIModel


class NCBITaxonomyScrapper:
    """Scrapper of html response from NCBI taxonomy info page of a given tax_id."""

    model = NCBITaxonomyAPIModel

    def __init__(self, html_content_info: bytes):
        """
        Instantiate your scrapper directly on html page content.

        Args:
            html_content_info: HTML content of retrieved page
        """
        self.soup_info = BeautifulSoup(html_content_info, features="html.parser")

    def result_found(self):
        """
        Check is result is found based on html tag.

        If <h1> is present in the page, it means an error message is returned.
        """
        if self.soup_info.h1 is not None:
            return False
        return True

    @classmethod
    def extract_tax_id_from_url(self, url: str):
        """Obtain taxonomy ID from url."""
        qparams = url.split("?", maxsplit=1)[1]
        for qparam in qparams.split("&"):
            if "id=" in qparam:
                return qparam.split("=")[-1]

    def retrieve_current_item(self):
        """Retrieve taxonomy item of interest from the page."""
        table_of_interest = self.soup_info.body.find_all("table")[3]
        page_title = self.soup_info.find_all("title")[0].text
        name = page_title[page_title.find("(") + 1 : page_title.find(")")]  # noqa
        tax_id = table_of_interest.tr.td.text.split("Taxonomy ID:", maxsplit=1)[
            -1
        ].split()[0]
        rank = table_of_interest.find_all("strong")[-2].text
        current_item = {"rank": rank, "tax_id": tax_id, "name": name}
        return current_item

    def retrieve_hierarchy(self):
        """Retrieve taxonomy hierarchy from the page."""
        hierarchy = []
        for i in self.soup_info.dd.find_all("a"):
            hierarchy.append(
                {
                    "rank": i["title"],
                    "tax_id": self.extract_tax_id_from_url(i["href"]),
                    "name": i.text,
                }
            )
        return hierarchy

    def scrap(self):
        """Perform scrapping of the content of interest."""
        self.entry = {}
        self.entry["current_item"] = self.retrieve_current_item()
        self.entry["hierarchy"] = self.retrieve_hierarchy()

    @property
    def validated_entry(self) -> dict:
        """
        Get validated entry from the scrapper as a dict.

        Returns:
            Validated entry in the model described in dabeplech
        """
        if getattr(self, "entry", None) is None:
            self.scrap()
        return self.model(**self.entry)
