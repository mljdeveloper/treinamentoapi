from ttunit.views import CreateUnitAPIView, TTUnitDetailAPIView
from django.urls import path

urlpatterns = [
    path("", CreateUnitAPIView.as_view(), name="unit"),
    path("<int:id>", TTUnitDetailAPIView.as_view(), name="units"),

]
