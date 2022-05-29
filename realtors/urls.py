from realtors import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("realtors/", views.RealtorList.as_view()),
    path("realtors/<slug:slug>/", views.RealtorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
