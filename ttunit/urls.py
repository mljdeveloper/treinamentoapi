from ttunit.views import CreateUnitAPIView, TTUnirDetailAPIView
from django.urls import path

urlpatterns = [
    path("", CreateUnitAPIView.as_view(), name="unit"),
    path("<int:id>", TTUnirDetailAPIView.as_view(), name="units")
]
