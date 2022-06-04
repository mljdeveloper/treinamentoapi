from course.views import CourseAPIView, CourseDetailAPIView
from django.urls import path

urlpatterns = [
    path("", CourseAPIView.as_view(), name="addcourses"),
    path("<int:id>", CourseDetailAPIView.as_view(), name="detcourse")
]
