from django.urls import path
from .views import  TaskTrack

urlpatterns = [
    path('', TaskTrack.as_view(), name='tasks'),
]
