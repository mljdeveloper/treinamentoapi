from Instructor.views import InstructorAPIView, InstructorDetailAPIView
from django.urls import path

urlpatterns = [
    path("", InstructorAPIView.as_view(), name="instructors"),
    path("<int:id>", InstructorDetailAPIView.as_view(), name="instructor")
]
