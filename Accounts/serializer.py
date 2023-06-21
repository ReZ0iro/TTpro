from rest_framework import serializers 

from django.contrib.auth import get_user_model

#

class UserSerializer(serializers.ModelSerializer) : 

    class Meta : 

        model     = get_user_model()
        fields    = "__all__"

class CreateAdminUserSerializer(serializers.ModelSerializer) :
    class Meta : 
        model   = get_user_model()
        fields  = ("first_name" , "last_name" , "username" , "email"  , "password")

        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self,validated_data) : 
            user = get_user_model().objects.create_admin(
                 
                validated_data["username"] ,
                validated_data["email"] ,
                validated_data["first_name"] , 
                validated_data["last_name"] ,
                validated_data["password"] , 

            )
            return user

class CreateUserSerializer(serializers.ModelSerializer) : 

    class Meta : 
        model   = get_user_model()
        fields  = ("username", "email", "first_name", "last_name")

        extra_kwargs = {"password" : {"write_only" : True}}
    def create(self,validated_data) : 

        user    = get_user_model().objects.create_user(     
             validated_data["username"] , 
             validated_data["email"]    ,
             validated_data["first_name"] ,
             validated_data["last_name"] ,
        )

        return user
    