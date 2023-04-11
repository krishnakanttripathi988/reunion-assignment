from pymongo import MongoClient
from utils.api_configs import ApiConfigs

class DatabaseService:
    client = None
    db = None
    def __init__(self):
        if DatabaseService.client is None:
            DatabaseService.client = MongoClient(ApiConfigs.DB_URL) 
            DatabaseService.db = DatabaseService.client[ApiConfigs.DB_NAME]
    
    @staticmethod
    def get_user():
        if DatabaseService.db is None:
            DatabaseService()
        return DatabaseService.db['users']
    
