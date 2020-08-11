from dabeplech.base import BaseAPI, GETMixin


class PDBeAPI(BaseAPI, GETMixin):
    BASE_URL = "https://www.ebi.ac.uk/pdbe/api/"


class PDBeUniprotMappingAPI(PDBeAPI):
    ROUTE = "mappings/uniprot/"


class PDBePFAMMappingAPI(PDBeAPI):
    ROUTE = "mappings/pfam/"
