from rest_framework import serializers 

from django.contrib.auth import get_user_model

#

class CreateAdminUserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model   = get_user_model()
        fields  = ("first_name" , "last_name" , "username" , "email" , "phone_number")

        extra_kwargs = {'password' : {'write_only' : True}}

        def create(self,validated_data) : 
            user = get_user_model().objects.create_admin(
                validated_data["username"] ,
                validated_data["email"] ,
                validated_data["first_name"] , 
                validated_data["last_name"] ,
                validated_data["phone_number"] ,
                validated_data["password"] , 
            )
            return user