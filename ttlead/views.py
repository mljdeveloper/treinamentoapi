from ttlead.pagination import CustomPageNumberPagination
from ttunit.models import TTUnit
from ttlead.models import TTlead
from rest_framework.permissions import IsAuthenticated
from .serializers import TTleadSerializer
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


class CreateLeadAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']

    def post(self, request, format=None):
        serializer = TTleadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TTLeadDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTleadSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return TTlead.objects.all()


class CompanyLeadDetailAPIView(generics.ListAPIView):
    serializer_class = TTleadSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()  # return empty queryset
        typeofuser = self.request.user.typeofuser

        if typeofuser == 'C':
            return TTlead.objects.all().filter(parent_id=self.request.user.id)
        else:
            return TTlead.objects.all().filter(username=self.request.user.id)
