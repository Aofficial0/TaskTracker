from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskTrack(LoginRequiredMixin, ListView):
    model = Task 
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name= 'task'
    template_name= 'core/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task 
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')