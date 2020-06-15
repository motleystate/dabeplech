from urllib.parse import urljoin

from requests.exceptions import HTTPError

from bioapi.base import BaseAPI
from bioapi.parsers.kegg import KeggOrthologyParser


ALLOWED_DATABASES = [
    'pathway', 'brite', 'module', 'ko', 'genome', 'organism', 'vg', 'ag', 'compound',
    'glycan', 'reaction', 'rclass', 'enzyme', 'network', 'variant', 'disease',
    'drug', 'dgroup', 'environ'
]


class KEGGAPI(BaseAPI):
    BASE_URL = 'http://rest.kegg.jp'
    LIST_PARSER = {}
    GET_PARSER = {
        'ko': KeggOrthologyParser
    }

    def get_all(self, database, params=None):
        if database not in ALLOWED_DATABASES:
            raise Exception(f"<{database}> not a valid database for KEGG. Must choose among {ALLOWED_DATABASES}")
        full_url = urljoin(self.url, f"list/{database}")
        response = self.session.get(full_url, params=params)
        self.last_url_requested = full_url
        response.raise_for_status()
        if self.LIST_PARSER.get(database, None) is not None:
            return self.LIST_PARSER.get(database)(response.text)
        return response.text

    def get(self, entry_id, params=None):
        full_url = urljoin(self.url, f"get/{entry_id}")
        response = self.session.get(full_url, params=params)
        self.last_url_requested = full_url
        response.raise_for_status()
        database = response.text.splitlines()[0].split()[-1].lower()
        if self.GET_PARSER.get(database, None) is not None:
            parser = self.GET_PARSER.get(database)(response.text)
            parser.parse()
            return parser.validated_entry.dict()
        return response.text