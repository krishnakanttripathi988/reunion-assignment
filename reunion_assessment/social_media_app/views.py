from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from social_media_app.service.user_service import UserService
from social_media_app.utils.helper import Authentication
from social_media_app.models import *

authenticator = Authentication()

class Authenticate(APIView):
    
    def post(self,request):
        try:
            data = request.data
            return Response(data={'token': UserService.getUserAuthenticated(data.get("email_id"),data.get("password"))}, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class Follow(APIView):
    def post(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            results = User.objects.filter(user_id=int(id))
            followed_user = results[0]
            return Response(data={'message': UserService.followUser(current_user,followed_user)}, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
