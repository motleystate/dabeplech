"""DOI API service."""
from dabeplech.base import BaseAPI, GETMixin


class DOIAPI(BaseAPI, GETMixin):
    """DOI API service (https://dx.doi.org)."""

    BASE_URL = "https://dx.doi.org"
    HEADERS = {
        "Content-type": "application/json",
        "Accept": "application/vnd.citationstyles.csl+json",
    }
