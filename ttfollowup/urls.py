from .views import CreateFollowUpAPIView, TTLeadDetailAPIView, BrokerFollowupDetailAPIView, LeadFollowupDetailAPIView
from django.urls import path, re_path


urlpatterns = [
    path("", CreateFollowUpAPIView.as_view(), name="addcompany"),
    path("<int:id>", TTLeadDetailAPIView.as_view(), name="detcompany"),
    re_path('^broker/(?P<id>.+)/$', BrokerFollowupDetailAPIView.as_view()),
    re_path('^lead/(?P<id>.+)/$', LeadFollowupDetailAPIView.as_view()),

]
