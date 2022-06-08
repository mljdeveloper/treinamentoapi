from ttfollowup.pagination import CustomPageNumberPagination
from ttfollowup.models import TTfollowup
from rest_framework.permissions import IsAuthenticated
from .serializers import TTFollowupSerializer
from django.shortcuts import get_object_or_404
from authentication.models import User
from django.contrib.auth import authenticate
from rest_framework import response, status, permissions, filters
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ttcompany.models import TTCompany
from rest_framework import generics


class CreateFollowUpAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']

    def post(self, request, format=None):
        serializer = TTFollowupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TTLeadDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTFollowupSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return TTfollowup.objects.all()


class BrokerFollowupDetailAPIView(generics.ListAPIView):
    serializer_class = TTFollowupSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TTfollowup.objects.all().filter(broker=self.request.user)


class LeadFollowupDetailAPIView(generics.ListAPIView):
    serializer_class = TTFollowupSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        lead_id = self.kwargs['id']
        return TTfollowup.objects.all().filter(lead=lead_id)
