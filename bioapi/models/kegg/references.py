from typing import List

from pydantic import AnyUrl, BaseModel


class KeggReferenceModel(BaseModel):
    authors: List[str]
    title: str
    journal: str
    doi: str = None
    sequence: List[str] = None
