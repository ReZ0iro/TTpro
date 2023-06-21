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
    """
    
    Its For SuperAdmin TO Create And Add Admin To App !
    
    """

    def post(self,request) :
        
        serializers = CreateAdminUserSerializer(data= request.data)

        serializers.is_valid(raise_exception=True)

        user = serializers.save()

        serializers = UserSerializer(user)

        return Response(serializers.data , status=status.HTTP_201_CREATED)
class AddUserByAdmin(APIView) :
    """
    
    Its For Admin And SuperAdmin To Add Users By them selfs !
    
    """
    def post(self, request) : 

        serializers     = CreateUserSerializer(data=request.data)

        serializers.is_valid(raise_exception=True)

        user = serializers.save()

        serializers = UserSerializer(user)

        return Response(serializers.data , status=status.HTTP_201_CREATED)


class UsersList(APIView) : 

    """

    it show the users list for Admin And SuperAdmin !
    
    """
    def get(self,request) : 

        first_query = UserListQueries()

        serializers = UserSerializer(first_query , many = True)

        return Response(serializers.data , status=status.HTTP_200_OK)

class UserDetails(APIView) : 
    """

    it show the user Details for admin and superadmin 
    And they can change sth on the user
    
    """
    def get(self, request, id) : 

        the_user    = TheUserDetailsQuery(id = id)

        serializers = UserSerializer(the_user)

        return Response(serializers.data , status=status.HTTP_200_OK)
    
    def put(self, request, id) : 
        """

        Its For Changeing UserDetails !By Admin And SuperAdmin !

        """

        the_user    = TheUserDetailsQuery(id = id)

        serializers = UserSerializer(the_user, data = request.data, partial = True)

        serializers.is_valid(raise_exception=True)
        
        serializers.save()

        return Response(serializers.data, status = status.HTTP_202_ACCEPTED)