from typing import List

from pydantic import BaseModel


class NCBITaxonomyItemModel(BaseModel):
    tax_id: int
    rank: str
    name: str


class NCBITaxonomyAPIModel(BaseModel):
    current_item: NCBITaxonomyItemModel
    hierarchy: List[NCBITaxonomyItemModel]
