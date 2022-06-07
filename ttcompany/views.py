
from ttcompany.models import TTCompany
from rest_framework.permissions import IsAuthenticated
from .serializers import TTCompanySerializer, TTUnitSerializers
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
from ttunit.models import TTUnit
from django.views.generic import View
from rest_framework import generics


class CreateCompanyAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']

    def post(self, request, format=None):
        serializer = TTCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTCompanySerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return TTCompany.objects.filter(username=self.request.user)


class CompanyUnitDetailAPIView(generics.ListAPIView):
    serializer_class = TTUnitSerializers

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        unitid = self.kwargs['id']
        return TTUnit.objects.all().filter(company=unitid)
