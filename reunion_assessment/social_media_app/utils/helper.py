from functools import wraps
from django.shortcuts import redirect
from rest_framework.response import Response
from social_media_app.utils.api_configs import ApiConfigs
from social_media_app.models import User
import time, jwt, json


class ReunionHelper:
    @staticmethod
    def validate_token_data(data:dict):
        try:
            email = data.get('email')
            password = data.get('password')
            return email,password
        except:
            raise ValueError("Please insert valid token")
    @staticmethod
    def generate_id_prefix(prefix:str):
        return prefix+str(time.time_ns())



class Authentication:
    def __init__(self):
        self.users = User.objects

    def get_authenticated(self,request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if not auth:
            return Response(data={'message': 'Authentication required'}, status= 401)
        auth_header_parts = auth.split()
        if len(auth_header_parts) != 2 or auth_header_parts[0].lower() != 'bearer':
            # Invalid authorization header format
            return Response(data={'message': 'Invalid authorization header'}, status= 401)
        token = auth_header_parts[1]
        data = jwt.decode(token, ApiConfigs.JWT_SECRET, algorithms=['HS256'])
        try:
            email, password = ReunionHelper.validate_token_data(data)
        except ValueError:
            return Response(data={'message': 'Invalid bearer token'}, status= 401)
        results = self.users.filter(email=email)
        check = True
        authenticated_user = None
        for result in results:
            if result.password == password:
                authenticated_user = result
                check = False
        if check:
            return {'message': 'Invalid email or password'}, 401

        return authenticated_user