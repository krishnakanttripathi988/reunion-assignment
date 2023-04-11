from flask import Flask, request
from functools import wraps
from utils.api_configs import ApiConfigs
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
    def __init__(self, users):
        self.users = users

    def __call__(self, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            auth = request.headers.get('Authorization')
            if not auth:
                return {'message': 'Authentication required'}, 401
            auth_header_parts = auth.split()
            if len(auth_header_parts) != 2 or auth_header_parts[0].lower() != 'bearer':
                # Invalid authorization header format
                return {'message': 'Invalid authorization header'}, 401
            token = auth_header_parts[1]
            data = jwt.decode(token, ApiConfigs.JWT_SECRET, algorithms=['HS256'])
            try:
                email, password = ReunionHelper.validate_token_data(data)
            except ValueError:
                return {'message': 'Invalid bearer token'}, 401
            results = self.users.find({'email':email})
            check = True
            authenticated_uid = None
            for result in results:
                if result['password'] == password:
                    authenticated_uid = result['_id']
                    check = False
            if check:
                return {'message': 'Invalid email or password'}, 401

            return func(authenticated_uid,*args, **kwargs)
        return decorated_function