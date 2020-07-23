from typing import List, Dict

from pydantic import BaseModel


class KeggLinksModel(BaseModel):
    links: Dict[str, List[str]]
