from .views import CreateLeadAPIView, TTLeadDetailAPIView, CompanyLeadDetailAPIView
from django.urls import path, re_path


urlpatterns = [
    path("", CreateLeadAPIView.as_view(), name="addlead"),
    path("<int:id>", TTLeadDetailAPIView.as_view(), name="detlead"),
    re_path('^leads/(?P<id>.+)/$', CompanyLeadDetailAPIView.as_view()),

]
