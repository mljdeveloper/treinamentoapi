from ttunit.pagination import CustomPageNumberPagination
from ttunit.models import TTUnit
from rest_framework.permissions import IsAuthenticated
from .serializers import TTUnitSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from authentication.models import User
from ttcompany.models import TTCompany
from django.contrib.auth import authenticate
from rest_framework import response, status, permissions, filters
from authentication.serializers import LoginSerializer, RegisterSerializer
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class CreateUnitAPIView(ListCreateAPIView):
    serializer_class = TTUnitSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'price', 'bedroom',
                        'restroom', 'unittype', 'city']
    search_fields = ['id']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return TTUnit.objects.none()
        return TTUnit.objects.filter(username=self.request.user)


"""     def post(self, request, format=None):
        serializer = TTUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


class TTUnitDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTUnitSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        typeofuser = self.request.user.typeofuser
        if typeofuser == 'C':
            return TTUnit.objects.all().filter(parent_id=self.request.user)
        else:
            return TTUnit.objects.all().filter(username_id=self.request.user)


class UnitListAPIView(generics.ListAPIView):
    serializer_class = TTUnitSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):

        unitid = self.kwargs['id']
        typeofuser = self.request.user.typeofuser

        Objeto = User.objects.all().get(id=unitid)

        if typeofuser == 'C':
            return TTUnit.objects.all().filter(parent_id=Objeto)
        else:
            return TTUnit.objects.all().filter(username_id=Objeto)
