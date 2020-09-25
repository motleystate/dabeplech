from dabeplech.base import BaseAPI, GETMixin


class DOIAPI(BaseAPI, GETMixin):
    BASE_URL = "https://dx.doi.org"
    HEADERS = {
        'Content-type': 'application/json',
        'Accept': 'application/vnd.citationstyles.csl+json'
    }
