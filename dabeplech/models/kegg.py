"""Model descriptions for KEGG."""
from typing import Dict, List

from pydantic import BaseModel, Field


class BaseKeggModel(BaseModel):
    """Base model for KEGG entry."""

    entry_id: str
    names: List[str]


class BaseKeggListModel(BaseModel):
    """Base model for list of KEGG entries."""

    entries: List[BaseKeggModel]


class KeggReferenceModel(BaseModel):
    """Description for a KEGG reference item."""

    authors: List[str] = None
    title: str
    journal: str
    pubmed_id: int = None
    doi: str = None
    sequence: List[str] = None


class DBLinksModel(BaseModel):
    """Description for a KEGG dblink item."""

    GO: List[str] = None
    COG: List[str] = None
    RN: List[str] = None


class KeggLinksModel(BaseModel):
    """Description for a KEGG links."""

    links: Dict[str, List[str]]


class BaseKeggWithRefModel(BaseKeggModel):
    """Base model for KEGG entry with references."""

    references: List[KeggReferenceModel] = None


class KeggOrthologyModel(BaseKeggWithRefModel):
    """Description for a KEGG orthology entry."""

    entry_id: str = Field(regex=r"^K\d{5}$")
    definition: str = None
    modules: dict = None
    ec_numbers: List[str] = None  # noqa
    pathways: dict = None
    genes: dict = None
    dblinks: DBLinksModel = None
    diseases: dict = None


class LightKeggOrthologyModel(BaseKeggModel):
    """Light description for a KEGG orthology entry."""

    definition: str = None
    ec_numbers: List[str] = None  # noqa


class KeggOrthologyListModel(BaseModel):
    """Description for list of KEGG orthologies."""

    entries: List[LightKeggOrthologyModel]


class KeggPathwayModel(BaseKeggWithRefModel):
    """Description for a KEGG pathway entry."""

    entry_id: str = Field(regex=r"^(map|ko)\d{5}$")
    description: str = None
    classes: List[str] = None
    modules: dict = None
    pathway_maps: dict = None
    orthologies: dict = None
    compounds: dict = None
    related_pathways: dict = None
    ko_pathway: str = Field(None, regex=r"^ko\d{5}$")
    dblinks: DBLinksModel = None
    diseases: dict = None


class KeggPathwayListModel(BaseKeggListModel):
    """Description for list of KEGG pathways."""

    pass


class KeggModuleModel(BaseKeggWithRefModel):
    """Description for a KEGG module entry."""

    entry_id: str = Field(regex=r"^M\d{5}$")
    definition: str = None
    orthologies: dict = None
    classes: List[str] = None
    pathways: dict = None
    reactions: dict = None
    compounds: dict = None
    rmodules: dict = None
    comment: str = None


class KeggModuleListModel(BaseKeggListModel):
    """Description for list of KEGG modules."""

    pass
