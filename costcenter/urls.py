from costcenter.views import (CostCenterAPIView,
                              CostCenterDetailAPIView)


from django.urls import path

urlpatterns = [
    path("", CostCenterAPIView.as_view(), name="costcenters"),
    path("<int:id>", CostCenterDetailAPIView.as_view(), name="costcenter")
]
