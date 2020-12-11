"""HAL API service."""
from urllib.parse import urljoin

from dabeplech.base import BaseAPI, GETMixin


class HALAPI(BaseAPI, GETMixin):
    """HAL API service (https://api.archives-ouvertes.fr/search/)."""

    BASE_URL = "https://api.archives-ouvertes.fr/search/"

    def find(self, doi: str):
        """
        Perform FIND operation.

        Args:
            doi: the DOI of the searched document
        Returns:
            response from HAL API
        """
        full_url = urljoin(self.url, f'?fq=doiId_s:"{doi}"&fl=*&wt=json')
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()

    def get(self, hal_id: int):
        """
        Perform GET operation.

        Args:
            hal_id: the HAL ID of adocument
        Returns:
            response from HAL API
        """
        full_url = urljoin(self.url, f"hal?q=docid:{hal_id}&fl=*&wt=json")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()
