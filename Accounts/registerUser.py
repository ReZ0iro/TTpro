from django.contrib.auth import get_user_model

# rest_framework :

from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response

# Serializer :

from Accounts.serializer import RegisterationSerializer , UserSerializer

# Registeration Codes : 

class RegisterationAPI(APIView) :

    def post(self, request) :

        serializers = RegisterationSerializer(data = request.data)

        serializers.is_valid(raise_exception=True)

        user = serializers.save()

        serializers = UserSerializer(user)

        return Response(serializers.data , status = status.HTTP_201_CREATED)