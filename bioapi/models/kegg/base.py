from typing import List

from pydantic import BaseModel

from bioapi.models.kegg.dblinks import DBLinksModel
from bioapi.models.kegg.references import KeggReferenceModel


class BaseKeggModel(BaseModel):
    entry_id: str
    name: str
    modules: dict = None
    dblinks: DBLinksModel = None
    references: List[KeggReferenceModel] = None