from authentication import views
from .views import UserOwnerDetailAPIView, UserOwnerByFirstName, PersonListAPIView
from django.urls import path, re_path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('user', views.AuthUserAPIView.as_view(), name='user'),
    path('list', views.UserAPIView.as_view(), name='list'),
    re_path('^owner/$', UserOwnerDetailAPIView.as_view()),
    re_path('^search_fn/(?P<first_name>.+)/$', UserOwnerByFirstName.as_view()),
    re_path('^lista/$',
            PersonListAPIView.as_view(), name='personlist'),

]
