"""
URL configuration for reunion_assessment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from social_media_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authenticate', Authenticate.as_view()),
    path('api/follow/<id>',Follow.as_view()),
    path('api/unfollow/<id>',Authenticate.as_view()),
    path('api/user',Authenticate.as_view()),
    path('api/posts',Authenticate.as_view()),
    path('api/posts/<id>',Authenticate.as_view()),
    path('api/like/<id>',Authenticate.as_view()),
    path('api/unlike/<id>',Authenticate.as_view()),
    path('api/comment/<id>',Authenticate.as_view()),
    path('api/all_posts',Authenticate.as_view()),
]
