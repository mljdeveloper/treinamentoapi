from .views import CreateCompanyAPIView, CompanyDetailAPIView, CompanyUnitDetailAPIView, \
    CompanyUserDetailApiView, CompanyUserRUD
from django.urls import path, re_path


urlpatterns = [
    path("", CreateCompanyAPIView.as_view(), name="addcompany"),
    path("<int:id>", CompanyDetailAPIView.as_view(), name="detcompany"),
    re_path('^units/(?P<id>.+)/$', CompanyUnitDetailAPIView.as_view()),
    re_path('^user/(?P<id>.+)/$', CompanyUserDetailApiView.as_view()),
    re_path('^userRUD/(?P<id>.+)/$', CompanyUserRUD.as_view())

]
