from position.views import PositionAPIView, PositionDetailAPIView
from django.urls import path

urlpatterns = [
    path("", PositionAPIView.as_view(), name="position"),
    path("<int:id>", PositionDetailAPIView.as_view(), name="position")
]
