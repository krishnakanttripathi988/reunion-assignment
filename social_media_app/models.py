from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    user_id = models.IntegerField(primary_key=True)
    followers = models.CharField(max_length=200000,default=None,null=True, blank=True)
    following = models.CharField(max_length=200000,default=None,null=True, blank=True)
    posts = models.CharField(max_length=2000000000,default=None,null=True, blank=True)
    liked_posts = models.CharField(max_length=200000,default=None,null=True, blank=True)


    def __str__(self):
        return self.email

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    number_of_likes = models.IntegerField(default=0, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=200000,default=None, null=True, blank=True)

    def __str__(self):
        return self.id

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=200)
    username = models.CharField(max_length=50)