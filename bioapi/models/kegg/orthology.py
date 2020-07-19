from typing import List

from pydantic import BaseModel, Field

from .base import BaseKeggModel, LightBaseKeggModel


class KeggOrthologyModel(BaseKeggModel):
    entry_id: str = Field(regex=r"^K\d{5}$")
    definition: str = None
    ec_numbers: List[str] = None  # noqa
    pathways: dict = None
    genes: dict = None


class LightKeggOrthologyModel(LightBaseKeggModel):
    definition: str = None
    ec_numbers: List[str] = None  # noqa


class KeggOrthologyListModel(BaseModel):
    entries: List[LightKeggOrthologyModel]
