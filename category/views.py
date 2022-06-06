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
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Category.objects.none()
        return Category.objects.filter(username=self.request.user)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Category.objects.none()  # return empty queryset
        return Category.objects.filter(username=self.request.user)
