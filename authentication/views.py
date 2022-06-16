from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from authentication.serializers import LoginSerializer, RegisterSerializer, TTownerSerializers
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from authentication.models import User
from ttcompany.models import TTCompany
from ttowner.models import TTowner
from django.db import IntegrityError
from rest_framework.parsers import MultiPartParser, FormParser
from authentication.pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework import generics
# Create your views here.


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RegisterSerializer

    def get(self, request):
        user = request.user

        serializer = RegisterSerializer(user)

        return response.Response({'user': serializer.data})


class CorpRegisterAPIView(GenericAPIView):
    permission_classes = [permissions.AllowAny, ]
    authentication_classes = []
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(
            data=request.data)

        if serializers.is_valid():
            serializers.save()

            return response.Response(serializers.data, status=status.HTTP_201_CREATED)

        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = RegisterSerializer

    def post(self, request):
        if self.request.user.typeofuser == 'C':
            objuser = User.objects.all().get(username=self.request.user.username)
            varuseremail = request.data['email']

        serializers = self.serializer_class(
            data=request.data)

        if serializers.is_valid():
            serializers.save()

        if self.request.user.typeofuser == 'C':
            objUpdateUser = User.objects.get(email=varuseremail)
            objUpdateUser.parent_id = objuser
            objUpdateUser.save()

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


class UserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegisterSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (permissions.IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):

        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()  # return empty queryset
        typeofuser = self.request.user.typeofuser

        userid = self.kwargs['id']
        print(userid)
        objUser = User.objects.all().get(id=userid)
        print(objUser)
        print(self.request.data.get('password', None))
        objUser.set_password(self.request.data.get('password', None))
        objUser.save()

        if typeofuser == 'C':
            return User.objects.all().filter(parent_id=self.request.user)
        else:
            return User.objects.all().filter(username_id=self.request.user)


class UserOwnerDetailAPIView(generics.ListAPIView):
    serializer_class = TTownerSerializers

    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        typeofuser = self.request.user.typeofuser

        if typeofuser == 'C':
            return User.objects.all().filter(parent_id=self.request.user)
        else:
            return User.objects.all().filter(username_id=self.request.user)


class PersonListAPIView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'username']
    search_fields = ['id']
    ordering_fields = ['id']

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return User.objects.none()

        typeofuser = self.request.user.typeofuser

        if typeofuser == 'C':
            return User.objects.all().filter(parent_id=self.request.user)
        else:
            return User.objects.all().filter(username_id=self.request.user)
