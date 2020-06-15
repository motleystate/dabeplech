from urllib.parse import urljoin

import requests


class BaseAPI(object):
    BASE_URL = ''
    ROUTE = ''
    HEADERS = {
        'Content-type': 'application/json',
        'Accept': '*/*'
    }
    SESSION = requests.Session

    def __init__(self):
        if not getattr(self, 'base_url', None):
            self.base_url = self.BASE_URL
        if not getattr(self, 'route', None):
            self.route = self.ROUTE
        self.url = urljoin(self.base_url, self.route)
        self.last_url_requested = None
        self.session = self.SESSION()
        self.session.headers.update(self.HEADERS)


class LISTMixin:

    def get_all(self, params=None):
        response = self.session.get(self.url, params=params)
        self.last_url_requested = self.url
        response.raise_for_status()
        return response.json()


class GETMixin:

    def get(self, entry_id, params=None):
        full_url = urljoin(self.url, entry_id)
        response = self.session.get(full_url, params=params)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()


class POSTMixin:

    def post(self, data):
        response = self.session.post(f"{self.url}", json=data)
        self.last_url_requested = self.url
        response.raise_for_status()
        return response.json()


class PUTMixin:

    def put(self, data, entry_id=None):
        if entry_id:
            full_url = urljoin(self.url, entry_id + '/')
        else:
            full_url = self.url
        response = self.session.put(f"{full_url}", json=data)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()
