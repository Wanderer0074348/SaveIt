from fastapi import APIRouter, HTTPException
from database.models.link import LinkModel, LinkResponse
from database.operations import LinkOperations
from typing import List

router = APIRouter()

@router.post("/", response_model=dict)
async def create_link(link: LinkModel):
    try:
        link_id = await LinkOperations.create_link(link)
        return {"id": link_id, "message": "Link created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[LinkResponse])
async def get_links():
    try:
        return await LinkOperations.get_all_links()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{link_id}", response_model=LinkResponse)
async def get_link(link_id: str):
    try:
        link = await LinkOperations.get_link_by_id(link_id)
        if not link:
            raise HTTPException(status_code=404, detail="Link not found")
        return link
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
