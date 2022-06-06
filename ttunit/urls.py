from ttunit.views import CreateUnitAPIView, TTUnitDetailAPIView, TTUnitDetalhes
from django.urls import path

urlpatterns = [
    path("", CreateUnitAPIView.as_view(), name="unit"),
    path("<int:id>", TTUnitDetailAPIView.as_view(), name="units"),
    path("unit/<int:id>", TTUnitDetalhes.as_view(), name="detunit"),
]
