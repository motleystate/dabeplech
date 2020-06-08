from typing import List

from pydantic import BaseModel, Field

from bioapi.models.kegg.dblinks import DBLinksModel
from bioapi.models.kegg.references import KeggReferenceModel


class KeggModel(BaseModel):
    entry_id: str
    name: str
    classes: List[str] = None
    dblinks: DBLinksModel = None
    pathways: dict = None
    modules: dict = None
    genes: dict = None
    references: List[KeggReferenceModel] = None


class KeggOrthologyModel(KeggModel):
    entry_id: str = Field(regex="^K\d{5}$")
    names: List[str] = None
    definition: str = None
    diseases: dict = None


class KeggPathwayModel(KeggModel):
    entry_id: str = Field(regex='^(map|ko)\d{5}$')
    description: str
    diseases: dict = None
    orthologs: dict = None
    organism: str = None
    enzymes: list = None
    reactions: dict = None
    compounds: dict = None
    rel_pathways: dict = None
    ko_pathway: str = Field(None, regex='^ko\d{5}$')
