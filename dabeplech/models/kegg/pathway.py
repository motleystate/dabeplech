from typing import List

from pydantic import BaseModel, Field

from dabeplech.models.kegg.dblinks import DBLinksModel
from .base import BaseKeggModel


class KeggPathwayModel(BaseKeggModel):
    entry_id: str = Field(regex=r'^(map|ko)\d{5}$')
    description: str = None
    classes: List[str] = None
    modules: dict = None
    pathway_maps: dict = None
    orthologies: dict = None
    compounds: dict = None
    related_pathways: dict = None
    ko_pathway: str = Field(None, regex=r'^ko\d{5}$')
    dblinks: DBLinksModel = None
    diseases: dict = None


class KeggPathwayListModel(BaseModel):
    entries: List[BaseKeggModel]
