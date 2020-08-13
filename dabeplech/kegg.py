from typing import Union

import logging
from urllib.parse import urljoin

from dabeplech.base import BaseAPI
from dabeplech.parsers.kegg import (
    KeggOrthologyParser, KeggOrthologyListParser,
    KeggPathwayParser, KeggPathwayListParser, KeggLinkParser,
    KeggModuleParser, KeggModuleListParser
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
    _LIST_PARSER: dict = {
        'ko': KeggOrthologyListParser,
        'pathway': KeggPathwayListParser,
        'module': KeggModuleListParser,
    }
    _GET_PARSER: dict = {
        'ko': KeggOrthologyParser,
        'pathway': KeggPathwayParser,
        'module': KeggModuleParser,
    }

    def _check_db(self, database: str):
        if database not in self.ALLOWED_DATABASES:
            raise Exception(f"<{database}> not a valid database for KEGG. Must choose among {self.ALLOWED_DATABASES}")

    def list(self, database: str, get_model: bool = True) -> Union[dict, str]:
        """
        :param database: selected database you want to retrieve all content from (list in self.ALLOWED_DATABASES)
        :param get_model: return pydantic model (return dict if False)
        :return: response from KEGG API for the database (can be Pydantic model format too)
        """
        self._check_db(database)
        full_url = urljoin(self.url, f"list/{database}")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        if self._LIST_PARSER.get(database, None) is not None:
            parser = self._LIST_PARSER.get(database)(response.text)
            parser.parse()
            if get_model:
                return parser.validated_model
            return parser.validated_model.dict()
        else:
            logger.warning("Parser not defined yet for %s, returning plain text", database)
        return response.text

    def find(self, database: str, query: str, get_model: bool = True) -> Union[dict, str]:
        """
        :param database: selected database you want to query (list in self.ALLOWED_DATABASES)
        :param query: query you want to find in the chosen db
        :param get_model: return pydantic model (return dict if False)
        :return: response from KEGG API for the database (can be Pydantic model format too)
        """
        self._check_db(database)
        full_url = urljoin(self.url, f"find/{database}/{query}")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        if self._LIST_PARSER.get(database, None) is not None:
            parser = self._LIST_PARSER.get(database)(response.text)
            parser.parse()
            if get_model:
                return parser.validated_model
            return parser.validated_model.dict()
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

    def link_db(self, target_db: str, source_db: str, get_model: bool = True) -> Union[dict, str]:
        """
        :param target_db: selected target database (list in self.ALLOWED_DATABASES)
        :param source_db: selected source database (list in self.ALLOWED_DATABASES)
        :param get_model: return pydantic model (return dict if False)
        :return: response from KEGG API for the database (can be Pydantic model format too)
        """
        self._check_db(target_db)
        self._check_db(source_db)
        full_url = urljoin(self.url, f"link/{target_db}/{source_db}")
        validated_entry = self._perform_link_request(full_url)
        if get_model:
            return validated_entry
        return validated_entry.dict()

    def link_entries(self, target_db: str, db_entries: str, get_model: bool = True) -> Union[dict, str]:
        """
        :param target_db: selected target database (list in self.ALLOWED_DATABASES)
        :param db_entries: selected entries (several entry can be specified using + operator)
        :param get_model: return pydantic model (return dict if False)
        :return: response from KEGG API for the database (can be Pydantic model format too)
        """
        self._check_db(target_db)
        full_url = urljoin(self.url, f"link/{target_db}/{db_entries}")
        validated_entry = self._perform_link_request(full_url)
        if get_model:
            return validated_entry
        return validated_entry.dict()

    def get(self, entry_id: str, get_model: bool = True) -> Union[dict, str]:
        """
        :param entry_id: KEGG ID to retrieve.
        :param get_model: return pydantic model (return dict if False)
        :return: response from KEGG API for the given entry_id (can be Pydantic model format too)
        """
        full_url = urljoin(self.url, f"get/{entry_id}")
        response = self.session.get(full_url)
        self.last_url_requested = full_url
        response.raise_for_status()
        database = response.text.splitlines()[0].split()[-1].lower()
        if self._GET_PARSER.get(database, None) is not None:
            parser = self._GET_PARSER.get(database)(response.text)
            parser.parse()
            if get_model:
                return parser.validated_entry
            return parser.validated_entry.dict()
        else:
            logger.warning("Parser not defined yet for %s, returning plain text", database)
        return response.text
