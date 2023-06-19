from django.urls import path 
from posts.views import *
#

urlpatterns = [
     path("posts/<int:id>/" , UserPosts.as_view()) ,
]
