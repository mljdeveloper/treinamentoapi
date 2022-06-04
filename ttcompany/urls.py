from .views import CreateCompanyAPIView, CompanyDetailAPIView
from django.urls import path

urlpatterns = [
    path("", CreateCompanyAPIView.as_view(), name="addcompany"),
    path("<int:id>", CompanyDetailAPIView.as_view(), name="detcompany")
]
