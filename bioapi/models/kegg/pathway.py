from typing import List

from pydantic import Field

from .base import BaseKeggModel


class KeggPathwayModel(BaseKeggModel):
    entry_id: str = Field(regex=r'^(map|ko)\d{5}$')
    classes: List[str] = None
    pathway_maps: dict = None
    diseases: dict = None
    orthologs: dict = None
    compounds: dict = None
    related_pathways: dict = None
    ko_pathway: str = Field(None, regex=r'^ko\d{5}$')