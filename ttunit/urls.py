from ttunit.views import TTUnitList, CreateUnitAPIView, TTUnitDetailAPIView
from django.urls import path, re_path

urlpatterns = [
    path("", CreateUnitAPIView.as_view(), name="unit"),
    path("<int:id>", TTUnitDetailAPIView.as_view(), name="units"),
    re_path('^lista/(?P<id>.+)/$', TTUnitList.as_view()),

]
