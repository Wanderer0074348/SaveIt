from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone

class FolderModel(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
class FolderResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    parent_id: Optional[str]
    created_at: datetime
    updated_at: datetime
