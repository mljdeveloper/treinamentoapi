from frequency.pagination import CustomPageNumberPagination
from frequency.serializers import FrequencySerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from frequency.models import Frequency
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class FrequencyAPIView(ListCreateAPIView):
    serializer_class = FrequencySerializer
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
            return Frequency.objects.none()
        return Frequency.objects.filter(username=self.request.user)


class FrequencyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FrequencySerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return Frequency.objects.filter(username=self.request.user)
