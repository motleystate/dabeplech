import logging
from urllib.parse import urljoin

import requests

_LOGGER = logging.getLogger(__name__)


class LoggedSession(requests.Session):

    def request(self, method, url, **kwargs):
        _LOGGER.info(f"{method.upper()} {url}")
        response = super().request(method, url, **kwargs)
        _LOGGER.info(f"STATUS CODE: {response.status_code}")
        return response


class BaseAPI(object):
    BASE_URL = ''
    ROUTE = ''
    HEADERS = {
        'Content-type': 'application/json',
        'Accept': '*/*'
    }
    SESSION = LoggedSession

    def __init__(self):
        if not getattr(self, 'base_url', None):
            self.base_url = self.BASE_URL
        if not getattr(self, 'route', None):
            self.route = self.ROUTE
        self.url = urljoin(self.base_url, self.route)
        self.session = self.SESSION()
        self.session.headers.update(self.HEADERS)

    def get_all(self, params=None):
        response = self.session.get(self.url, params=params)
        response.raise_for_status()
        return response.json()

    def get(self, entry_id):
        full_url = urljoin(self.url, entry_id)
        response = self.session.get(full_url)
        response.raise_for_status()
        return response.json()

    def post(self, data):
        response = self.session.post(f"{self.url}", json=data)
        response.raise_for_status()
        return response.json()

    def put(self, data, entry_id=None):
        if entry_id:
            full_url = urljoin(self.url, entry_id)
        else:
            full_url = self.url
        response = self.session.put(f"{full_url}/", json=data)
        response.raise_for_status()
        return response.json()
