from django.shortcuts import render

# rest_framework : 

from rest_framework.views import APIView 
from rest_framework.response import Response
# Queries :
from posts.queries import *

# Serializer : 
from posts.serializer import *

# Create your views here.

class UserPosts(APIView) : 
    def get(self, request, id) : 

        first_query = UserContentPostsQueries(id = id )

        serializer  =UserPostsSerializer(first_query , many = True)

        return Response(serializer.data)