from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.


class Tasklist(ListView):
    model = Task
    context_object_name ='task_list'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = 'base/task_detail_change.html'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task_delete"
    success_url = reverse_lazy('tasks')
