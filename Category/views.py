from category.pagination import CustomPageNumberPagination
from category.serializers import CategorySerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from category.models import Category
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'categoryname']
    search_fields = ['id', 'categoryname']
    ordering_fields = ['id', 'categoryname']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return Category.objects.filter(username=self.request.user)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return Category.objects.filter(username=self.request.user)
