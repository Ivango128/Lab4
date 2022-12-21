from typing import List
from pydantic import BaseModel
from datetime import datetime

class Notes_text(BaseModel):
    id: int
    text: str = None

class Notes_info(BaseModel):
    creat: datetime
    updated: datetime

class Notes_create(BaseModel):
    id: int

class Notes_list(BaseModel):
    notes_list:List[int]