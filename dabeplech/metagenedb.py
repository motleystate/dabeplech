"""MetageneDB API services."""
from .base import BaseAPI, LISTMixin, GETMixin, POSTMixin, PUTMixin


class BaseMetageneDBAPI(BaseAPI):
    """Base for MetageneDB API services (https://metagenedb.pasteur.cloud/)."""

    BASE_URL = "https://metagenedb.pasteur.cloud/"

    def __init__(self, base_url=BASE_URL, jwt_token=None):
        """
        Instantiate with non mandatory jwt token.

        Args:
            base_url: base url to use (could be local instance)
            jwt_token: JWT token for AUTH
        """
        self.base_url = base_url
        super().__init__()
        if jwt_token is not None:
            self.session.headers.update({"Authorization": f"JWT {jwt_token}"})


class MetageneDBTokenAPI(BaseMetageneDBAPI, POSTMixin):
    """MetageneDB API service for JWT token generation."""

    ROUTE = "api/auth/obtain_token/"


class MetageneDBAPI(BaseMetageneDBAPI, LISTMixin, GETMixin, POSTMixin, PUTMixin):
    """Base for MetageneDB API service to DB."""

    pass


class MetageneDBCatalogGeneAPI(MetageneDBAPI):
    """MetageneDB API service for genes."""

    ROUTE = "api/catalog/v1/genes/"


class MetageneDBCatalogTaxonomyAPI(MetageneDBAPI):
    """MetageneDB API service for taxonomy."""

    ROUTE = "api/catalog/v1/taxonomy/"


class MetageneDBCatalogFunctionAPI(MetageneDBAPI):
    """MetageneDB API service for functions."""

    ROUTE = "api/catalog/v1/functions/"


class MetageneDBCatalogKeggOrthologyAPI(MetageneDBAPI):
    """MetageneDB API service for kegg orthologies."""

    ROUTE = "api/catalog/v1/kegg-orthologies/"


class MetageneDBCatalogEggNOGAPI(MetageneDBAPI):
    """MetageneDB API service for eggnogs."""

    ROUTE = "api/catalog/v1/eggnogs/"


class MetageneDBCatalogStatisticsAPI(MetageneDBAPI):
    """MetageneDB API service for statistics."""

    ROUTE = "api/catalog/v1/statistics/"
