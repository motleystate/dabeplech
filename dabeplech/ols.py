from dabeplech.base import BaseAPI, GETMixin


class OLSAPI(BaseAPI, GETMixin):
    BASE_URL = "https://www.ebi.ac.uk/ols/api/ontologies/go/terms/"

    def get_term(self, entry_id: str):
        """
        Perform GET request to the service using the ontology term ID only

        :param entry_id: short ID of the ontology concept (e.g. GO_0008150)
        :param params: query params for the request
        """
        return self.get(
            f"http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F{entry_id}"
        )
