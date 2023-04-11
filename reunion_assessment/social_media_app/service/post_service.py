import time
from social_media_app.models import *
from social_media_app.serializers import *
from rest_framework.response import Response



class PostService:
    
    @staticmethod
    def populate_comments(data:dict):
        list_of_comments = []
        comments = data.get('comments')
        if comments is None:
            return list_of_comments
        for item in comments.split(","):
            if item is None or item is "":
                continue
                
            try:
                comment = Comment.objects.get(comment_id=str(item))
                list_of_comments.append(CommentSerializer(comment).data)
            except Comment.DoesNotExist:
                print("Comment not present for given ID")
        return list_of_comments


    @staticmethod
    def upload_post(title:str,description:str, current_user:User):
        id = str(int(time.time()))
        post = Post(post_id=id,title=title, description=description)
        post.save()
        if current_user.posts is None:
            current_user.posts = ""
        current_user.posts+=","+str(id)
        current_user.save(force_update=True)
        return PostSerializer(post).data
    
    @staticmethod
    def delete_post(id:str,current_user:User):
        if current_user.posts is None or ","+str(id) not in current_user.posts:
            return Response(data={"error":"You are not authorised to delete this post"},status=403)
        try:
            post = Post.objects.get(post_id=id)
            post.delete()
            current_user.posts = current_user.posts.replace(","+str(id),"")
        except Post.DoesNotExist:
            return Response(data={"message":"Post doesn't exist"}, status=400)
        return Response(data={"message":"Post deleted"}, status=400)
    
    @staticmethod
    def get_post(id:str,current_user:User):
        if current_user.posts is None or ","+str(id) not in current_user.posts:
            return Response(data={"error":"You are not authorised to delete this post"},status=403)
        
        try:
            post = Post.objects.get(post_id=id)
            data = AllPostSerializer(post).data
            data['comments'] = PostService.populate_comments(data)
            return Response(data=data, status=400)
        except Post.DoesNotExist:
            return Response(data={"message":"Post doesn't exist"}, status=400)
        
    @staticmethod
    def like_post(id:str,current_user:User):
        try:
            post = Post.objects.get(post_id=id)
            if post.number_of_likes is None:
                post.number_of_likes =0
            post.number_of_likes+=1
            if current_user.liked_posts is None:
                current_user.liked_posts = ""
            if ","+str(id) in current_user.liked_posts:
                return Response(data={"message":"You haven already liked the post"}, status=400)
            post.save(force_update=True)
            current_user.liked_posts += ","+str(id)
            current_user.save(force_update=True)
            return Response(data={"message":"Post Liked"}, status=200)
        except Post.DoesNotExist:
            return Response(data={"message":"Post doesn't exist"}, status=400)
        
    @staticmethod
    def unlike_post(id:str,current_user:User):
        try:
            post = Post.objects.get(post_id=id)
            if current_user.liked_posts is None or ","+str(id) not in current_user.liked_posts:
                return Response(data={"message":"You haven't liked the post"}, status=400)
            if post.number_of_likes is None:
                post.number_of_likes =0
            post.number_of_likes-=1
            current_user.liked_posts = current_user.liked_posts.replace(","+str(id),"")
            current_user.save(force_update=True)
            post.save(force_update=True)
            return Response(data={"message":"Post Unliked"}, status=200)
        except Post.DoesNotExist:
            return Response(data={"message":"Post doesn't exist"}, status=400)
        
    @staticmethod
    def comment_post(id:str,comment:str,current_user:User):
        comment_id = str(int(time.time()))
        comment = Comment(comment_id=comment_id,comment = comment)
        try:
            post = Post.objects.get(post_id=id)
            if post.comments is None:
                post.comments = ""
            comment.username = current_user.username
            post.comments+=","+str(comment_id)
            comment.save()
            post.save(force_update=True)
            return Response(data={"message":"Post Commented"}, status=400)
        except Post.DoesNotExist:
            return Response(data={"message":"Post doesn't exist"}, status=400)
        
    @staticmethod
    def get_all_post(current_user:User):
        posts = current_user.posts
        data = []
        for item in posts.split(","):
            if item is None or item is "":
                continue
            try:
                post = Post.objects.get(post_id=str(item))
                result = AllPostSerializer(post).data
                result['comments'] = PostService.populate_comments(result)
                data.append(result)

            except Post.DoesNotExist:
                print("Post not present for given ID")
        return Response(data={"posts":data}, status=200)

