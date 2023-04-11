from rest_framework import serializers
from social_media_app.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id','title','description','created_time']

class AllPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment','username']