from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from funcao.models import Funcao


class TestListCreateFuncao(APITestCase):

    def authenticate(self):

        self.client.post(reverse('register'), {"email": "eusou100555@hotmail.com",
                                               "username": "eusou100555",
                                               "password": "30304040",
                                               "parent_id": 1})

        response = self.client.post(
            reverse('login'), {'email': "eusou100555@hotmail.com", 'password': "30304040"})

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

    def test_should_not_create_funcao_with_no_auth(self):
        sample_funcao = {"nomefuncao": "Jogador"}
        response = self.client.post(reverse('funcoes'), sample_funcao)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_funcao_with_auth(self):
        self.authenticate()
        sample_funcao = {"nomefuncao": "Jogador"}
        response = self.client.post(reverse('funcoes'), sample_funcao)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
