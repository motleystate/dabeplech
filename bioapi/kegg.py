import logging
from urllib.parse import urljoin

from bioapi.base import BaseAPI
from bioapi.parsers.kegg import (
    KeggOrthologyParser, KeggOrthologyListParser,
    KeggPathwayParser, KeggPathwayListParser,
)

logging.basicConfig()
logger = logging.getLogger()


class KEGGAPI(BaseAPI):
    ALLOWED_DATABASES: list = [
        'pathway', 'brite', 'module', 'ko', 'genome', 'organism', 'vg', 'ag', 'compound',
        'glycan', 'reaction', 'rclass', 'enzyme', 'network', 'variant', 'disease',
        'drug', 'dgroup', 'environ'
    ]
    BASE_URL: str = 'http://rest.kegg.jp'
    LIST_PARSER: dict = {
        'ko': KeggOrthologyListParser,
        'pathway': KeggPathwayListParser,
    }
    GET_PARSER: dict = {
        'ko': KeggOrthologyParser,
        'pathway': KeggPathwayParser,
    }

    def get_all(self, database: str):
        """
        :param database: selected database you want to retrieve all content from (list in self.ALLOWED_DATABASES)
        :return: response from KEGG API for the database
        :rtype: *dict* **IF** parser available **ELSE** *str*
        """
        if database not in self.ALLOWED_DATABASES:
            raise Exception(f"<{database}> not a valid database for KEGG. Must choose among {self.ALLOWED_DATABASES}")
        full_url = urljoin(self.url, f"list/{database}")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        if self.LIST_PARSER.get(database, None) is not None:
            parser = self.LIST_PARSER.get(database)(response.text)
            parser.parse()
            return parser.validated_model
        else:
            logger.warning("Parser not defined yet for %s, returning plain text", database)
        return response.text

    def get(self, entry_id: str, get_model=True):
        """
        :param entry_id: KEGG ID to retrieve.
        :return: response from KEGG API for the given entry_id
        :rtype: *dict* **IF** parser available **ELSE** *str*
        """
        full_url = urljoin(self.url, f"get/{entry_id}")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        database = response.text.splitlines()[0].split()[-1].lower()
        if self.GET_PARSER.get(database, None) is not None:
            parser = self.GET_PARSER.get(database)(response.text)
            parser.parse()
            if get_model:
                return parser.validated_entry
            return parser.validated_entry.dict(exclude_none=True)
        else:
            logger.warning("Parser not defined yet for %s, returning plain text", database)
        return response.text
