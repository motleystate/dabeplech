import logging
from urllib.parse import urljoin

from bioapi.base import BaseAPI
from bioapi.parsers.kegg import (
    KeggOrthologyParser, KeggOrthologyListParser,
    KeggPathwayParser, KeggPathwayListParser, KeggLinkParser
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

    def _check_db(self, database: str):
        if database not in self.ALLOWED_DATABASES:
            raise Exception(f"<{database}> not a valid database for KEGG. Must choose among {self.ALLOWED_DATABASES}")

    def list(self, database: str):
        """
        :param database: selected database you want to retrieve all content from (list in self.ALLOWED_DATABASES)
        :return: response from KEGG API for the database
        :rtype: *json* **IF** parser available **ELSE** *str*
        """
        self._check_db(database)
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

    def find(self, database: str, query: str):
        """
        :param database: selected database you want to query (list in self.ALLOWED_DATABASES)
        :return: response from KEGG API for the database
        :rtype: *json* **IF** parser available **ELSE** *str*
        """
        self._check_db(database)
        full_url = urljoin(self.url, f"find/{database}/{query}")
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

    def _perform_link_request(self, full_url: str):
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        parser = KeggLinkParser(response.text)
        parser.parse()
        return parser.validated_entry

    def link_db(self, target_db: str, source_db: str):
        """
        :param target_db: selected target database (list in self.ALLOWED_DATABASES)
        :param source_db: selected source database (list in self.ALLOWED_DATABASES)
        :return: response from KEGG API for the database
        :rtype: *json* **IF** parser available **ELSE** *str*
        """
        self._check_db(target_db)
        self._check_db(source_db)
        full_url = urljoin(self.url, f"link/{target_db}/{source_db}")
        return self._perform_link_request(full_url)

    def link_entries(self, target_db: str, db_entries: str):
        """
        :param target_db: selected target database (list in self.ALLOWED_DATABASES)
        :param db_entries: selected entries (several entry can be specified using + operator)
        :return: response from KEGG API for the database
        :rtype: *json* **IF** parser available **ELSE** *str*
        """
        self._check_db(target_db)
        full_url = urljoin(self.url, f"link/{target_db}/{db_entries}")
        return self._perform_link_request(full_url)

    def get(self, entry_id: str, get_model: bool = True):
        """
        :param entry_id: KEGG ID to retrieve.
        :return: response from KEGG API for the given entry_id
        :rtype: *json* **IF** parser available **ELSE** *str*
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
