from .base import (
    BaseAPI, LISTMixin, GETMixin, POSTMixin, PUTMixin
)


class BaseMetageneDBAPI(BaseAPI):
    BASE_URL = 'https://metagenedb.pasteur.cloud/'

    def __init__(self, base_url=BASE_URL, jwt_token=None):
        self.base_url = base_url
        super().__init__()
        if jwt_token is not None:
            self.session.headers.update({
                'Authorization': f"JWT {jwt_token}"
            })


class MetageneDBTokenAPI(BaseMetageneDBAPI, POSTMixin):
    ROUTE = 'api/auth/obtain_token/'


class MetageneDBAPI(BaseMetageneDBAPI, LISTMixin, GETMixin, POSTMixin, PUTMixin):
    pass


class MetageneDBCatalogGeneAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/genes/'


class MetageneDBCatalogTaxonomyAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/taxonomy/'


class MetageneDBCatalogFunctionAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/functions/'


class MetageneDBCatalogKeggOrthologyAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/kegg-orthologies/'


class MetageneDBCatalogEggNOGAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/eggnogs/'


class MetageneDBCatalogStatisticsAPI(MetageneDBAPI):
    ROUTE = 'api/catalog/v1/statistics/'
