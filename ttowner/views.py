from ttunit.pagination import CustomPageNumberPagination
from ttowner.models import TTowner
from rest_framework.permissions import IsAuthenticated
from .serializers import TTownerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from authentication.models import User
from django.contrib.auth import authenticate
from rest_framework import response, status, permissions, filters
from authentication.serializers import LoginSerializer, RegisterSerializer
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ttcompany.models import TTCompany
from rest_framework import generics


class CreateOwnerAPIView(ListCreateAPIView):
    serializer_class = TTownerSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'first_name', 'last_name']
    search_fields = ['id', 'first_name', 'last_name']
    ordering_fields = ['first_name']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return TTowner.objects.none()
        return TTowner.objects.filter(username=self.request.user)


class TTownerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTownerSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return TTowner.objects.all().filter(username=self.request.user)


class TTCompanyList(generics.ListAPIView):
    serializer_class = TTownerSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        #1 -C
        #3 -P
        unitid = self.kwargs['id']
        typeofuser = self.request.user.typeofuser

        if typeofuser == 'C':
            Objeto = TTCompany.objects.all().get(id=unitid)
        else:
            Objeto = User.objects.all().get(id=unitid)

        if typeofuser == 'C':
            return TTowner.objects.all().filter(company_id=Objeto)
        else:
            return TTowner.objects.all().filter(username_id=Objeto)
