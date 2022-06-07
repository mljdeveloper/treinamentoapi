from .views import CreateLeadAPIView, TTLeadDetailAPIView
from django.urls import path


urlpatterns = [
    path("", CreateLeadAPIView.as_view(), name="addlead"),
    path("<int:id>", TTLeadDetailAPIView.as_view(), name="detlead"),

]
