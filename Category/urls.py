from Category.views import CategoryAPIView, CategoryDetailAPIView
from django.urls import path

urlpatterns = [
    path("", CategoryAPIView.as_view(), name="categories"),
    path("<int:id>", CategoryDetailAPIView.as_view(), name="category")
]
