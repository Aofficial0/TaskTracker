from django.urls import path
from django.contrib import admin
from .views import (home, TaskTrack, TaskDetail, TaskCreate, TaskUpdate, 
                    DeleteView, CustomLoginView, RegisterPage, 
                    TaskDeleteConfirmView, LogoutConfirmView, 
                    update_task_complete_status)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    
    # Auth-related URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout-confirm/', LogoutConfirmView.as_view(), name='logout-confirm'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Task-related URLs
    path('', TaskTrack.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteConfirmView.as_view(), name='task-delete'),
    path('tasks/complete/<int:task_id>/', update_task_complete_status, name='update_task_complete'),

    # Home page URL
    path('home/', home, name='home'),
]