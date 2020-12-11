"""Base with abstract classes for all parsers."""
from abc import ABC, abstractmethod
from typing import Dict, List, Union

from pydantic import BaseModel


class BaseParser(ABC):
    """Base structure for parsers."""

    model = BaseModel  # Pydantic model to describe the response

    def __init__(self, content_response: str):
        """
        Instantiate your parser on the response.

        Args:
            content_response: content response from the API
        """
        self.parsed_content: Dict[str, Union[str, dict]] = {}
        self.lines = content_response.rstrip().split("\n")

    @abstractmethod
    def parse(self):
        """Perform parsing of the ``content_response``."""
        pass

    @property
    def validated_entry(self) -> BaseModel:
        """
        Retrieve entry validated with the model.

        Returns:
            Validated entry.
        """
        return self.model(**self.parsed_content)


class BaseListParser(ABC):
    """Base structure for parsers."""

    model = BaseModel  # Pydantic model to describe the response

    def __init__(self, content_response: str):
        """
        Instantiate your parser on the response.

        Args:
            content_response: content response from the API
        """
        self.parsed_content: List[dict] = []
        self.lines = content_response.rstrip().split("\n")

    @abstractmethod
    def parse(self):
        """Perform parsing of the ``content_response``."""
        pass

    @property
    def validated_model(self) -> BaseModel:
        """
        Retrieve entry validated with the model.

        Returns:
            Validated entry.
        """
        return self.model(entries=self.parsed_content)
