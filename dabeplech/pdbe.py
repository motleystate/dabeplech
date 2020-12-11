"""API services for PDBe."""
from dabeplech.base import BaseAPI, GETMixin


class PDBeAPI(BaseAPI, GETMixin):
    """Base for PDBe API (https://www.ebi.ac.uk/pdbe/api/)."""

    BASE_URL = "https://www.ebi.ac.uk/pdbe/api/"


class PDBeUniprotMappingAPI(PDBeAPI):
    """PDBe API for uniprot mapping route."""

    ROUTE = "mappings/uniprot/"


class PDBePFAMMappingAPI(PDBeAPI):
    """PDBe API for pfam mapping route."""

    ROUTE = "mappings/pfam/"
