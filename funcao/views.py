from funcao.pagination import CustomPageNumberPagination
from funcao.serializers import FuncaoSerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from funcao.models import Funcao
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class FuncaoAPIView(ListCreateAPIView):
    serializer_class = FuncaoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'nomefuncao']
    search_fields = ['id', 'nomefuncao']
    ordering_fields = ['id', 'nomefuncao']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user, superusuario=self.request.user.parent_id)

    def get_queryset(self):
        return Funcao.objects.filter(username=self.request.user)


class FuncaoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FuncaoSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return Funcao.objects.filter(username=self.request.user)
