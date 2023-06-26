from rest_framework import serializers 

from django.contrib.auth import get_user_model

#

class UserSerializer(serializers.ModelSerializer) : 

    class Meta : 

        model     = get_user_model()
        fields    = "__all__"       # IT should Change cuase when its all it show the password(HASHED!)

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
    
class RegisterationSerializer(serializers.ModelSerializer) :

    """
    Its For register serializing !
    It check the two password fields that should be equal !
    and thent it user the func in Accounts.UserAccountManager that is create_user !
    
    
    """ 

    password        = serializers.CharField(
        write_only  = True , 
        required    = True ,
    )

    password_2      = serializers.CharField(
        write_only  = True , 
        required    = True ,
    )

    class Meta : 

        model           = get_user_model()

        fields          = ("username", "email", "first_name", "last_name", "password", "password_2")

    def validate(self,attrs) : 
        if attrs["password"] != attrs["password_2"] : 
            raise serializers.ValidationError (
                {"password" : 'password field didnt match !'}
            )
        return attrs
    
    def create(self, validated_data):
        
        user = get_user_model().objects.create_user(
            username    = validated_data["username"]    , 
            email       = validated_data["email"]       , 
            first_name  = validated_data["first_name"]  ,
            last_name   = validated_data["last_name"]   ,
            password    = validated_data["password"]    ,

        )
        return user

