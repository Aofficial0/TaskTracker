from django.urls import path
from .views import  home, TaskTrack, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskDeleteConfirmView, LogoutConfirmView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout-confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskTrack.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteConfirmView.as_view(), name='task-delete'),
    
]
