from unittest import result
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "http://localhost:8000/api/"

# lista de produtos
#endpoint = "http://localhost:8000/api/listacargo/"
#get_response = requests.get(endpoint, json={"id": "1"})

#endpoint = "https://treinamentoapi.herokuapp.com//api/auth/register"
# get_response = requests.post(endpoint, json={
#                             "email": "marcos.luiz.jesus@hotmail.com", "username": "marcos", "password": "10102020"})

# salva funcao no banco
"""
hearder = {"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hcmNvcyIsImVtYWlsIjoibWFyY29zLmx1aXouamVzdXNAaG90bWFpbC5jb20iLCJleHAiOjE2ODMwNTYwOTd9.I9HOKQ2ph_baHosfB185LsJosSuvTAD5rvb_2Tk8JnQ"}
dados = {"nomefuncao": "pedreiro"}
get_response = requests.post(url='http://127.0.0.1:8080/api/funcao/',
                             headers=hearder,
                             json=dados
                             )
print(get_response.json())
"""


hearder = {"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im1hcmNvcyIsImVtYWlsIjoibWFyY29zLmx1aXouamVzdXNAaG90bWFpbC5jb20iLCJleHAiOjE2ODMwNTYwOTd9.I9HOKQ2ph_baHosfB185LsJosSuvTAD5rvb_2Tk8JnQ"}
dados = {"nomefuncao": "pedreiro"}
get_response = requests.get(url='http://127.0.0.1:8080/api/funcao/?id=1',
                            headers=hearder
                            )
print(get_response.json()['results'][-1]['nomefuncao'])


"""
usuario = requests.post('http://localhost:8080/api/auth/login', {
    'email': "marcos.luiz.jesus@hotmail.com",
    'password': "10102020"
})
print(usuario.json())
"""
