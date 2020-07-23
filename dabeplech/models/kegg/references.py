from typing import List

from pydantic import BaseModel


class KeggReferenceModel(BaseModel):
    authors: List[str] = None
    title: str
    journal: str
    pubmed_id: int = None
    doi: str = None
    sequence: List[str] = None
