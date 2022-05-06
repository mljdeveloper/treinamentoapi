from frequency.views import FrequencyAPIView, FrequencyDetailAPIView
from django.urls import path

urlpatterns = [
    path("", FrequencyAPIView.as_view(), name="frequencies"),
    path("<int:id>", FrequencyDetailAPIView.as_view(), name="frequency")
]
