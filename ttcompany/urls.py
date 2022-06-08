from .views import CreateCompanyAPIView, CompanyDetailAPIView, CompanyUnitDetailAPIView
from django.urls import path, re_path


urlpatterns = [
    path("", CreateCompanyAPIView.as_view(), name="addcompany"),
    path("<int:id>", CompanyDetailAPIView.as_view(), name="detcompany"),
    re_path('^units/(?P<id>.+)/$', CompanyUnitDetailAPIView.as_view()),
]
