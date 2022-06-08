from ttunitimage.models import TTUnitImage
from rest_framework.permissions import IsAuthenticated
from .serializers import TTUnitImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from authentication.models import User
from django.contrib.auth import authenticate
from rest_framework import response, status, permissions, filters
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import View
from rest_framework import generics


class CreateUnitImageAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser, FormParser]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'unit']
    search_fields = ['id', 'unit']
    ordering_fields = ['id', 'unit']

    def post(self, request, format=None):
        serializer = TTUnitImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnitImageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TTUnitImageSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return TTUnitImage.objects.all()


class GetAllUnitImagetDetailAPIView(generics.ListAPIView):
    serializer_class = TTUnitImageSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        unitid = self.kwargs['id']
        return TTUnitImage.objects.all().filter(unit=unitid)
