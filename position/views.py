from position.pagination import CustomPageNumberPagination
from position.serializers import PositionSerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from position.models import Position
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class PositionAPIView(ListCreateAPIView):
    serializer_class = PositionSerializer
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
        return Position.objects.filter(username=self.request.user)


class PositionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PositionSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return Position.objects.filter(username=self.request.user)
