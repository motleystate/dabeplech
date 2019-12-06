from .base import BaseAPI


class MetageneDBAPI(BaseAPI):
    BASE_URL = 'http://localhost/'

    def __init__(self, base_url=BASE_URL, jwt_token=None):
        self.base_url = base_url
        super().__init__()
        if jwt_token is not None:
            self.session.headers.update({
                'Authorization': f"JWT {jwt_token}"
            })


class MetageneDBCatalogGeneAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/genes/'


class MetageneDBCatalogTaxonomyAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/taxonomy/'


class MetageneDBCatalogFunctionAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/functions/'
