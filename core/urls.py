from django.urls import path
from .views import  TaskTrack, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskTrack.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]
