from typing import List

from pydantic import Field, constr

from .base import BaseKeggModel


class KeggOrthologyModel(BaseKeggModel):
    entry_id: str = Field(regex=r"^K\d{5}$")
    definition: str = None
    ec_numbers: List[constr(regex=r'^[0-9]\.[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}$')] = None  # noqa
    pathways: dict = None
    genes: dict = None