from typing import List

from pydantic import BaseModel


class DBLinksModel(BaseModel):
    GO: List[str] = None
    COG: List[str] = None
    RN: List[str] = None
