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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        context['count'] = queryset.filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            queryset = queryset.filter(title__icontains=search_input)

        status_filter = self.request.GET.get('status-filter') or 'all'
        if status_filter == 'incomplete':
            queryset = queryset.filter(complete=False)
        elif status_filter == 'complete':
            queryset = queryset.filter(complete=True)

        priority_filter = self.request.GET.get('priority-filter') or 'all'
        if priority_filter in ['high', 'medium', 'low']:
            queryset = queryset.filter(priority=priority_filter)

        context['tasks'] = queryset

        context['search_input'] = search_input
        context['status_filter'] = status_filter

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/task_detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete', 'priority']
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'priority']
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_form.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_confirm_delete.html'