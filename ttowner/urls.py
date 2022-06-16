from .views import CreateOwnerAPIView, TTownerDetailAPIView, TTOwnerList, UserOwnerByFirstName
from django.urls import path, re_path


urlpatterns = [
    path("", CreateOwnerAPIView.as_view(), name="addowner"),
    path("<int:id>", TTownerDetailAPIView.as_view(), name="detowner"),
    re_path('^lista/(?P<id>.+)/$', TTOwnerList.as_view()),
    re_path('^search_fn/(?P<first_name>.+)/(?P<id>.+)/$',
            UserOwnerByFirstName.as_view()),
]
