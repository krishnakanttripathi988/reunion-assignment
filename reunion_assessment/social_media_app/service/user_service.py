import jwt
from social_media_app.utils.api_configs import ApiConfigs
from social_media_app.models import *
class UserService:
    

    @staticmethod
    def getUserAuthenticated(email:str,password:str):
        auth_data = {"email":email,"password":password}
        token = jwt.encode(payload=auth_data,key=ApiConfigs.JWT_SECRET)
        return token
    

    @staticmethod
    def followUser(current_user:User,followed_uid:User):
        following = current_user.following
        followers = followed_uid.followers

        if following is None:
            following = ""
        if followers is None:
            followers = ""
        
        if ","+str(followed_uid.user_id) in following:
            return "Already Present"

        if current_user == followed_uid:
            return "Cannot follow to ourself"

        following+=","+str(followed_uid.user_id)
        followers+=","+str(current_user.user_id)
        

        current_user.following = following
        followed_uid.followers = followers

        current_user.save(force_update=True)
        followed_uid.save(force_update=True)

        return "Insert success"

        