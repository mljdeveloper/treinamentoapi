from .views import CreateFollowUpAPIView, TTLeadDetailAPIView, FollowupDetailAPIView, LeadFollowupDetailAPIView
from django.urls import path, re_path


urlpatterns = [
    path("", CreateFollowUpAPIView.as_view(), name="addcompany"),
    path("<int:id>", TTLeadDetailAPIView.as_view(), name="detcompany"),
    re_path('^username/(?P<id>.+)/$', FollowupDetailAPIView.as_view()),
    re_path('^lead/(?P<id>.+)/$', LeadFollowupDetailAPIView.as_view()),

]
