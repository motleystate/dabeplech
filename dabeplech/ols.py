"""OLS API services."""
from dabeplech.base import BaseAPI, GETMixin


class OLSAPI(BaseAPI, GETMixin):
    """OLS API service (https://www.ebi.ac.uk/ols/api/ontologies/go/terms/)."""

    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies/go/terms/"

    def get_term(self, entry_id: str):
        """
        Perform GET request to the service using the ontology term ID only.

        Args:
            entry_id: short ID of the ontology concept (e.g. GO_0008150)
            params: query params for the request
        """
        return self.get(
            f"http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F{entry_id}"
        )
