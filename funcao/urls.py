from funcao.views import FuncaoAPIView, FuncaoDetailAPIView
from django.urls import path

urlpatterns = [
    path("", FuncaoAPIView.as_view(), name="funcoes"),
    path("<int:id>", FuncaoDetailAPIView.as_view(), name="funcao")
]
