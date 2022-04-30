import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "http://localhost:8000/api/"

# lista de produtos
#endpoint = "http://localhost:8000/api/listacargo/"
#get_response = requests.get(endpoint, json={"id": "1"})

#endpoint = "https://treinamentoapi.herokuapp.com//api/auth/register"
# get_response = requests.post(endpoint, json={
#                             "email": "marcos.luiz.jesus@hotmail.com", "username": "marcos", "password": "10102020"})
endpoint = "https://treinamentoapi.herokuapp.com/api/funcao"
get_response = requests.post(endpoint, {"nomefuncao": "analista de desempenho nivel II"}
                             )
print(get_response.json())
