from typing import List

from pydantic import BaseModel

from dabeplech.models.kegg.references import KeggReferenceModel


class BaseKeggModel(BaseModel):
    entry_id: str
    names: List[str]


class BaseKeggListModel(BaseModel):
    entries: List[BaseKeggModel]


class BaseKeggWithRefModel(BaseKeggModel):
    references: List[KeggReferenceModel] = None
