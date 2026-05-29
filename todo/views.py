from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Task

class TaskLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task_list.html'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_confirm_delete.html'