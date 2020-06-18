from typing import List

from pydantic import BaseModel, Field, constr

from bioapi.models.kegg.dblinks import DBLinksModel
from bioapi.models.kegg.references import KeggReferenceModel


class KeggModel(BaseModel):
    entry_id: str
    name: str
    modules: dict = None
    dblinks: DBLinksModel = None
    references: List[KeggReferenceModel] = None


class KeggOrthologyModel(KeggModel):
    entry_id: str = Field(regex=r"^K\d{5}$")
    definition: str = None
    ec_numbers: List[constr(regex=r'^[0-9]\.[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}$')] = None  # noqa
    pathways: dict = None
    genes: dict = None


class KeggPathwayModel(KeggModel):
    entry_id: str = Field(regex=r'^(map|ko)\d{5}$')
    classes: List[str] = None
    pathway_maps: dict = None
    diseases: dict = None
    orthologs: dict = None
    compounds: dict = None
    related_pathways: dict = None
    ko_pathway: str = Field(None, regex=r'^ko\d{5}$')
