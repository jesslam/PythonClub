from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingDetails/<int:id>', views.meetingDetails, name='meetingdetails'),
]
