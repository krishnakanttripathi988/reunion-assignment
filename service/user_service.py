import jwt
from utils.api_configs import ApiConfigs
class UserService:
    

    @staticmethod
    def getUserAuthenticated(email:str,password:str):
        auth_data = {"email":email,"password":password}
        token = jwt.encode(payload=auth_data,key=ApiConfigs.JWT_SECRET)
        return token

        