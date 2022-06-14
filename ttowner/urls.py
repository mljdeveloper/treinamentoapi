from .views import CreateOwnerAPIView, TTownerDetailAPIView, TTCompanyList
from django.urls import path, re_path


urlpatterns = [
    path("", CreateOwnerAPIView.as_view(), name="addowner"),
    path("<int:id>", TTownerDetailAPIView.as_view(), name="detowner"),
    re_path('^lista/(?P<id>.+)/$', TTCompanyList.as_view())
]
