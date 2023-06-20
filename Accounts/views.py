from django.shortcuts import render

# rest_framework : 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

# serializers : 
from Accounts.serializer import * 

# Create your views here.

class AddAdminBySuperAdmin(APIView) :

    def post(self,request) :
        
        serializers = CreateAdminUserSerializer(data= request.data)

        serializers.is_valid(raise_exception=True)

        user = serializers.save()

        serializers = UserSerializer(user)

        return Response(serializers.data , status=status.HTTP_201_CREATED)