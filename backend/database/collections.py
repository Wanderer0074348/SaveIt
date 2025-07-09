from .connection import get_database

class Collections:
    def __init__(self):
        self.db = None
    
    async def initialize(self):
        self.db = await get_database()
        
    @property
    def users(self):
        return self.db.users
    
    @property
    def links(self):
        return self.db.links
    
    @property
    def folders(self):
        return self.db.folders

collections = Collections()
