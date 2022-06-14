from authentication import views
from .views import UserOwnerDetailAPIView, PersonListAPIView
from django.urls import path, re_path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('user', views.AuthUserAPIView.as_view(), name='user'),
    path("<int:id>", views.UserAPIView.as_view(), name='detail'),
    re_path('^owner/$', UserOwnerDetailAPIView.as_view()),
    re_path('^lista/$',
            PersonListAPIView.as_view(), name='personlist'),

]
