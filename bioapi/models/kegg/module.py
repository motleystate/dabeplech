from typing import List

from pydantic import BaseModel, Field

from .base import BaseKeggModel


class KeggModuleModel(BaseKeggModel):
    entry_id: str = Field(regex=r"^M\d{5}$")
    definition: str = None
    orthologies: dict = None
    classes: List[str] = None
    pathways: dict = None
    reactions: dict = None
    compounds: dict = None
    rmodules: dict = None
    comment: str = None


class KeggModuleListModel(BaseModel):
    entries: List[BaseKeggModel]
