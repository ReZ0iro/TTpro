from django.shortcuts import render

# rest_framework : 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters

# pagination : 
from Accounts.pagination import CustomPagination

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
    
class UserListPagination(ListAPIView) : 

    queryset            = UserListQueries()
    serializer_class    = UserSerializer
    pagination_class    = CustomPagination
    filter_backends     = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields       = [ "username" ,]
    ordering_fields     = ["id" , ]
    ordering            = ["id",]

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
    def delete(self, request, id) : 

        the_user    = TheUserDetailsQuery(id = id)
        
        the_user.delete()

        return Response(status=status.HTTP_200_OK)
        
    
class DeactiveUser(APIView) : 
    """

    Its FOr Deactive User By Admin And SuperAdmin !
    
    """
    def get(self, request, id) : 

        the_user    = TheUserDetailsQuery(id = id)

        mode = False


        if the_user.is_active == False : 

            mode = True

        serializers = UserSerializer(

            the_user , 

            data = {"is_active" : mode} ,

            partial = True ,

            )
        
        serializers.is_valid()

        serializers.save()

        return Response(serializers.data , status = status.HTTP_202_ACCEPTED)

class DeActiveUserByPostId(APIView) : 
    """

    Its FOr Deactive User By Admin And SuperAdmin !
    
    """

    def post(self, request) : 

        the_user    = TheUserDetailsQuery(id = request.data["id"])

        mode        = False 

        if the_user.is_active == False : 

            mode = True

        serializers = UserSerializer(

            the_user ,
            data    = {"is_active" : mode} , 
            partial = True

            )
        
        serializers.is_valid(raise_exception=True)

        serializers.save()

        return Response(serializers.data , status=status.HTTP_202_ACCEPTED)
        

