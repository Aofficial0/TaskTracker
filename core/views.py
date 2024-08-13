from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Task
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def home(request):
    # Renders the home page template
    return render(request, 'core/home.html')


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Displays a success message and redirects to the home page after login
        messages.success(self.request, 'You have successfully logged in.')
        return reverse_lazy('home')


class LogoutConfirmView(LoginRequiredMixin, View):
    template_name = 'core/logout-confirm.html'

    def get(self, request, *args, **kwargs):
        # Renders the logout confirmation page
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Logs out the user, displays a success message, and redirects to the login page
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect(reverse_lazy('login'))


def update_task_complete_status(request, task_id):
    # Toggles the completion status of a task and displays a success message
    task = get_object_or_404(Task, id=task_id)
    task.complete = not task.complete  # Toggle the complete status
    task.save()
    messages.success(request, f'Task "{task.title}" status updated successfully.')
    return redirect(request.META.get('HTTP_REFERER', '/'))


class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Registers a new user, logs them in, and displays a success message
        user = form.save()
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Registration successful. You are now logged in.')
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        # Redirects authenticated users to the tasks page
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskTrack(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        # Provides task data for the current user, including search functionality
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-bar') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task.html'
    # Displays detailed information about a specific task

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Creates a new task for the current user and displays a success message
        form.instance.user = self.request.user
        messages.success(self.request, 'Created task successful.')
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
         # Updates an existing task and displays a success message
        messages.success(self.request, 'Task updated successfully.')
        return super().form_valid(form)


class TaskDeleteConfirmView(LoginRequiredMixin, View):
    template_name = 'core/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

    def get(self, request, *args, **kwargs):
        # Renders a confirmation page for deleting a task
        task = Task.objects.get(id=kwargs['pk'])
        context = {
            'task': task
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Deletes the task and displays a success message
        task = Task.objects.get(id=kwargs['pk'])
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect(self.success_url)
