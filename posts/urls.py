from django.urls import path 
from posts.views import *
#

urlpatterns = [
     path("posts/<int:id>/" , TheUserPosts.as_view()) ,
     path("commmentThePost/" , CommentThePost.as_view())
]
