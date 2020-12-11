"""API like service for NCBI taxonomy."""
from typing import Union

import requests

from dabeplech.scrappers.ncbi_taxonomy import NCBITaxonomyScrapper


class NCBITaxonomyScrapAPI:
    """
    Scrap NCBI taxonomy pages to return information and mimic API behaviour.

    It retrieves useful information such as hierarchy of taxonomy.
    """

    HEADERS = {"Content-type": "text/html", "Accept": "*/*"}
    SESSION = requests.Session
    BASE_URL = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser"

    def __init__(self):
        """Instantiate NCBI API like service."""
        self.last_url_requested = None
        self.session = self.SESSION()
        self.session.headers.update(self.HEADERS)

    def get(
        self, tax_id: int, get_model: bool = True
    ) -> Union[NCBITaxonomyScrapper.model, dict]:
        """
        Perform GET like operation.

        Args:
            tax_id: NCBI taxonomy ID to retrieve data from
            get_model: return pydantic model (return dict if False)
        """
        full_url = f"{self.BASE_URL}/wwwtax.cgi?id={tax_id}&mode=info"
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        scrapper = NCBITaxonomyScrapper(response.content)
        if not scrapper.result_found():
            raise requests.exceptions.HTTPError(
                f"{tax_id} not found in NCBI taxonomy db."
            )
        if get_model:
            return scrapper.validated_entry
        return scrapper.validated_entry.dict()
