from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime

class LinkModel(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    description: Optional[str] = None
    tags: List[str] = []
    folder_id: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

class LinkResponse(BaseModel):
    id: str
    url: str
    title: Optional[str]
    description: Optional[str]
    tags: List[str]
    folder_id: Optional[str]
    created_at: datetime
    updated_at: datetime
