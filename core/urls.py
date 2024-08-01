from django.urls import path
from .views import  TaskTrack, TaskDetail, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskTrack.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    
]
