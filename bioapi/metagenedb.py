from .base import BaseAPI


class MetageneDBAPI(BaseAPI):
    BASE_URL = 'http://localhost/'

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        super().__init__()


class MetageneDBCatalogGeneAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/genes/'


class MetageneDBCatalogTaxonomyAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/taxonomy/'


class MetageneDBCatalogFunctionAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/functions/'
