from typing import List

from pydantic import AnyUrl, BaseModel


class KeggReferenceModel(BaseModel):
    authors: List[str]
    title: str
    journal: str
    volume: str = None
    issue: str = None
    pages: str = None
    year: int
    pubmed: str = None
    medline: str = None
    doi: str = None
    abstract: str = None
    url: AnyUrl
    mess: list = None
    embl_gb_record_number: str = None
    sequence_position: str = None
    comments: str = None
    affiliations: list = None
