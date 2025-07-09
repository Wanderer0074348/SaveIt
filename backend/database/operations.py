from .collections import collections
from .models.link import LinkModel, LinkResponse
from .models.folder import FolderModel, FolderResponse
from bson import ObjectId
from typing import List, Optional

class LinkOperations:
    @staticmethod
    async def create_link(link_data: LinkModel) -> str:
        # Convert the model to dict and handle HttpUrl conversion
        link_dict = link_data.dict()
        link_dict["url"] = str(link_dict["url"])  # Convert HttpUrl to string
        
        result = await collections.links.insert_one(link_dict)
        return str(result.inserted_id)
    
    @staticmethod
    async def get_all_links() -> List[LinkResponse]:
        cursor = collections.links.find()
        links = []
        async for document in cursor:
            document["id"] = str(document["_id"])
            del document["_id"]
            links.append(LinkResponse(**document))
        return links
    
    @staticmethod
    async def get_link_by_id(link_id: str) -> Optional[LinkResponse]:
        document = await collections.links.find_one({"_id": ObjectId(link_id)})
        if document:
            document["id"] = str(document["_id"])
            del document["_id"]
            return LinkResponse(**document)
        return None
