from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import LoginSerializer, RegisterSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from authentication.models import User

# Create your views here.


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = RegisterSerializer(user)

        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(
            data=request.data)

        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)

        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializers = self.serializer_class(user)

            return response.Response(serializers.data, status=status.HTTP_200_OK)

        return response.Response({"message": "Invalid Credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
