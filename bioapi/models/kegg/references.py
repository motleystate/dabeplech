from typing import List

from pydantic import BaseModel


class KeggReferenceModel(BaseModel):
    pubmed_id: int
    authors: List[str]
    title: str
    journal: str
    doi: str = None
    sequence: List[str] = None
