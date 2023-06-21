from django.shortcuts import render

# rest_framework : 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

# Serializers : 
from Accounts.serializer import * 

# Queries : 
from Accounts.queries import * 

# Create your views here.

class AddAdminBySuperAdmin(APIView) :

    def post(self,request) :
        
        serializers = CreateAdminUserSerializer(data= request.data)

        serializers.is_valid(raise_exception=True)

        user = serializers.save()

        serializers = UserSerializer(user)

        return Response(serializers.data , status=status.HTTP_201_CREATED)
class UsersList(APIView) : 
    def get(self,request) : 

        first_query = UserListQueries()
        
        serializers = UserSerializer(first_query , many = True)

        return Response(serializers.data , status=status.HTTP_200_OK)
