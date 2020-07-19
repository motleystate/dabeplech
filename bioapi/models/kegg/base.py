from typing import List

from pydantic import BaseModel

from bioapi.models.kegg.dblinks import DBLinksModel
from bioapi.models.kegg.references import KeggReferenceModel


class LightBaseKeggModel(BaseModel):
    entry_id: str
    names: List[str]


class BaseKeggModel(LightBaseKeggModel):
    modules: dict = None
    dblinks: DBLinksModel = None
    diseases: dict = None
    references: List[KeggReferenceModel] = None
