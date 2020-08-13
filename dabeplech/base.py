from urllib.parse import urljoin

import requests


class BaseAPI:
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
    """
    Corresponds to a ``GET`` that retrieve all items
    """

    def list(self, params: dict = None):
        """
        Perform GET request to the service

        :param params: query params for the request
        """
        response = self.session.get(self.url, params=params)
        self.last_url_requested = self.url
        response.raise_for_status()
        return response.json()


class GETMixin:
    """
    Corresponds to a ``GET`` that retrieve one item from its ID
    """

    def get(self, entry_id: str, params: dict = None):
        """
        Perform GET request to the service

        :param entry_id: ID of the entry you want to retrieve
        :param params: query params for the request
        """
        full_url = urljoin(self.url, entry_id)
        response = self.session.get(full_url, params=params)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()


class POSTMixin:

    def post(self, data: dict):
        """
        Perform POST request to the service

        :param data: data to send in the body of your POST
        """
        response = self.session.post(f"{self.url}", json=data)
        self.last_url_requested = self.url
        response.raise_for_status()
        return response.json()


class PUTMixin:

    def put(self, data: dict, entry_id: str = None):
        """
        Perform PUT request to the service

        :param data: data to send in the body of your PUT
        :param entry_id: ID of the entry you want to update
        """
        if entry_id:
            full_url = urljoin(self.url, entry_id + '/')
        else:
            full_url = self.url
        response = self.session.put(f"{full_url}", json=data)
        self.last_url_requested = full_url
        response.raise_for_status()
        return response.json()
