from Zipcode.pagination import CustomPageNumberPagination
from Zipcode.serializers import ZipcodeSerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from Zipcode.models import Zipcode
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ZipcodeAPIView(ListCreateAPIView):
    serializer_class = ZipcodeSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['zipcode']
    search_fields = ['zipcode']
    ordering_fields = ['zipcode']

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Zipcode.objects.order_by('-zipcode')


class ZipcodeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ZipcodeSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "zipcode"

    def get_queryset(self):
        return Zipcode.objects.All()
