import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from authentication.models import User
from authentication.serializers import LoginSerializer, RegisterSerializer


class LoginTestCase(APITestCase):
    def test_login(self):
        data = {
            "email": "marcos.luiz.jesus@hotmail.com",
            "password": "10102020"
        }
        print(data)

        response = self.client.post(
            "http://127.0.0.1:8080/api/auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
