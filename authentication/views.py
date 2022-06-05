from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from authentication.serializers import LoginSerializer, RegisterSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from authentication.models import User
from ttcompany.models import TTCompany
from django.db import IntegrityError
from rest_framework.parsers import MultiPartParser, FormParser
from authentication.pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
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
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(
            data=request.data)

        if serializers.is_valid():
            serializers.save()

            ObjUser = User.objects.get(
                username=request.data.get('username', '0'))

            typeofuser = request.data.get('typeofuser', '0')

            if typeofuser == 'C':

                first_name = ObjUser.first_name
                last_name = ObjUser.last_name
                full_name = '{} {}'.format(first_name, last_name)
                try:
                    TTCompany.objects.create(
                        contact=full_name.upper(),
                        username=ObjUser,
                    )

                except IntegrityError as e:
                    data = {'status': 1,
                            'mensagem': e.message}

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


class UserAPIView(ListAPIView):
    serializer_class = RegisterSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'username']
    search_fields = ['id', 'username']
    ordering_fields = ['id', 'username']

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
