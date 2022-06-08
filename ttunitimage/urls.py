from .views import CreateUnitImageAPIView, UnitImageDetailAPIView, GetAllUnitImagetDetailAPIView
from django.urls import path, re_path


urlpatterns = [
    path("", CreateUnitImageAPIView.as_view(), name="addunitimagem"),
    path("<int:id>", UnitImageDetailAPIView.as_view(), name="detunitimage"),
    re_path('^images/(?P<id>.+)/$', GetAllUnitImagetDetailAPIView.as_view()),
]
