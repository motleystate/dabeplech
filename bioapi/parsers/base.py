from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseParser(ABC):
    """
    Base structure for parsers
    """
    model = BaseModel  # Pydantic model to describe the response

    def __init__(self, content_response: str):
        """
        :param content_response: content response from the API
        """
        self.parsed_content = {}
        self.lines = content_response.rstrip().split('\n')

    @abstractmethod
    def parse(self):
        """
        Perform parsing of the ``content_response``
        """
        pass

    @property
    def validated_entry(self):
        """
        This property aims to return the entry, validated with the model

        :return: Validated entry.
        """
        return self.model(**self.parsed_content)


class BaseListParser(ABC):
    """
    Base structure for parsers
    """
    model = BaseModel  # Pydantic model to describe the response

    def __init__(self, content_response: str):
        """
        :param content_response: content response from the API
        """
        self.parsed_content = []
        self.lines = content_response.rstrip().split('\n')

    @abstractmethod
    def parse(self):
        """
        Perform parsing of the ``content_response``
        """
        pass

    @property
    def validated_model(self):
        """
        This property aims to return the model list, with the list accessible through entries attribute
        """
        return self.model(entries=self.parsed_content)
