from typing import List

from pydantic import BaseModel, Field

from .base import BaseKeggModel


class KeggPathwayModel(BaseKeggModel):
    entry_id: str = Field(regex=r'^(map|ko)\d{5}$')
    description: str = None
    classes: List[str] = None
    pathway_maps: dict = None
    orthologs: dict = None
    compounds: dict = None
    related_pathways: dict = None
    ko_pathway: str = Field(None, regex=r'^ko\d{5}$')


class KeggPathwayListModel(BaseModel):
    entries: List[KeggPathwayModel]
