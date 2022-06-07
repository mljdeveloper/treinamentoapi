from .views import CreateOwnerAPIView, TTownerDetailAPIView
from django.urls import path


urlpatterns = [
    path("", CreateOwnerAPIView.as_view(), name="addowner"),
    path("<int:id>", TTownerDetailAPIView.as_view(), name="detowner"),

]
