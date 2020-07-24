from typing import List

from pydantic import BaseModel, Field

from dabeplech.models.kegg.dblinks import DBLinksModel
from .base import BaseKeggModel, BaseKeggWithRefModel


class KeggOrthologyModel(BaseKeggWithRefModel):
    entry_id: str = Field(regex=r"^K\d{5}$")
    definition: str = None
    modules: dict = None
    ec_numbers: List[str] = None  # noqa
    pathways: dict = None
    genes: dict = None
    dblinks: DBLinksModel = None
    diseases: dict = None


class LightKeggOrthologyModel(BaseKeggModel):
    definition: str = None
    ec_numbers: List[str] = None  # noqa


class KeggOrthologyListModel(BaseModel):
    entries: List[LightKeggOrthologyModel]
