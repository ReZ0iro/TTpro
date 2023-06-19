from django.shortcuts import render

# rest_framework : 

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
# Queries :
from posts.queries import *

# Serializer : 
from posts.serializer import *

# Create your views here.

class TheUserPosts(APIView) : 

    def get(self, request, id) :

        first_query = UserContentPostsQueries(id = id )

        serializer  =UserPostsSerializer(first_query , many = True)

        return Response(serializer.data)
    
class CommentThePost(APIView) : 

    def post(self,request) :

        # user_id         = request.data["user_id"]  # cuase untill dont set auth and jwt stuffs !;

        # post_id         = request.data["post_id"]

        # text_comment    = request.data["text"]

        serializers = UserCommentsSerializer(data= request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        
        return Response(serializers.data , status=status.HTTP_201_CREATED)




