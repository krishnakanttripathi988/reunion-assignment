from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from social_media_app.service.user_service import UserService
from social_media_app.service.post_service import PostService
from social_media_app.utils.helper import Authentication
from social_media_app.serializers import UserSerializer
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
            if type(current_user) is Response:
                return current_user
            results = User.objects.filter(user_id=int(id))
            followed_user = results[0]
            return Response(data={'message': UserService.followUser(current_user,followed_user)}, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)

class UnFollow(APIView):
    def post(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            if type(current_user) is Response:
                return current_user
            results = User.objects.filter(user_id=int(id))
            followed_user = results[0]
            return Response(data={'message': UserService.unfollowUser(current_user,followed_user)}, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class GetUser(APIView):
    def get(self,request):
        try:
            current_user = authenticator.get_authenticated(request)
            if type(current_user) is Response:
                return current_user
            data = UserSerializer(current_user).data
            if current_user.followers is None:
                data['number_of_followers'] = 0
            else:
                data['number_of_followers'] = current_user.followers.count(",")
            if current_user.following is None:
                data['number_of_followings'] = 0
            else:
                data['number_of_followings'] = current_user.following.count(",")

            return Response(data=data, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class UploadPost(APIView):
    def post(self,request):
        try:
            current_user = authenticator.get_authenticated(request)
            data = request.data
            data = PostService.upload_post(data.get('title'),data.get('description'), current_user)
            return Response(data=data, status=200)
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class DeletePost(APIView):
    def delete(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            data = PostService.delete_post(id, current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
    def get(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            data = request.data
            data = PostService.get_post(id, current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)

class LikePost(APIView):
    def post(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            data = PostService.like_post(id, current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class UnLikePost(APIView):
    def post(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            data = PostService.unlike_post(id, current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)

class CommentPost(APIView):
    def post(self,request,id):
        try:
            current_user = authenticator.get_authenticated(request)
            comment = request.data
            data = PostService.comment_post(id,comment.get('comment'), current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)
        
class GetAllPost(APIView):
    def get(self,request):
        try:
            current_user = authenticator.get_authenticated(request)
            data = PostService.get_all_post(current_user)
            return data
        except Exception as e:
            return Response(data={'error': 'System Error occurred'},status=500)