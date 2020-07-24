from typing import List

from pydantic import Field

from .base import BaseKeggListModel, BaseKeggWithRefModel


class KeggModuleModel(BaseKeggWithRefModel):
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
    pass
