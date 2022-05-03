from Zipcode.views import ZipcodeAPIView, ZipcodeDetailAPIView
from django.urls import path

urlpatterns = [
    path("", ZipcodeAPIView.as_view(), name="zipcodes"),
    path("<int:id>", ZipcodeDetailAPIView.as_view(), name="zipcode")
]
