from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

# Create your views here.
class TaskTrack(ListView):
    model = Task 