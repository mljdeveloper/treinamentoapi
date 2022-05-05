from cost_center.pagination import CustomPageNumberPagination
from cost_center.serializers import CostCenterSerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from cost_center.models import CostCenter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CostCenterAPIView(ListCreateAPIView):
    serializer_class = CostCenterSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'costcenter']
    search_fields = ['id', 'costcenter']
    ordering_fields = ['id', 'costcenter']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return CostCenter.objects.filter(username=self.request.user)


class CostCenterDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CostCenterSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "costcenter"

    def get_queryset(self):
        return CostCenter.objects.filter(username=self.request.user)
