"""Describe built model from scrapper for NCBI Taxonomy."""
from typing import List

from pydantic import BaseModel


class NCBITaxonomyItemModel(BaseModel):
    """Description of an NCBI Taxonomy entry."""

    tax_id: int
    rank: str
    name: str


class NCBITaxonomyAPIModel(BaseModel):
    """Description of an NCBI Taxonomy response."""

    current_item: NCBITaxonomyItemModel
    hierarchy: List[NCBITaxonomyItemModel]
