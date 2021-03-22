"""OLS API services."""
from dabeplech.base import BaseAPI, GETMixin


class OLSGOAPI(BaseAPI, GETMixin):
    """OLS GO API service (https://www.ebi.ac.uk/ols/api/ontologies/go/terms/)."""

    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies/go/terms/"

    def get_term(self, entry_id: str):
        """
        Perform GET request to the service using the ontology term ID only.

        Args:
            entry_id: short ID of the ontology concept (e.g. GO_0008150)
        """
        return self.get(
            f"http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F{entry_id}"
        )


class OLSNCBITaxonomyAPI(BaseAPI, GETMixin):
    """OLS NCBI Taxonomy API service (https://www.ebi.ac.uk/ols/api/ontologies/ncbitaxon/terms/)."""

    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies/ncbitaxon/"

    def get(self, entry_id: str, params: dict = None) -> dict:
        """
        Perform GET request to the service.

        Args:
            entry_id: tax ID (e.g. 562)
            params: query params for the request
        """
        entry_id = f"terms?short_form=NCBITaxon_{entry_id}"
        return super().get(entry_id, params)
