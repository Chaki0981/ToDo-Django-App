from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import AddTaskForm, AddTaskFormAdvance

class GeneralTasksView():
    def post(self, request):
        form = AddTaskForm(request.POST)

        if form.is_valid():
            form.save()

        context = {
            'form': form,
        }

        return redirect('starting-page')

class TasksView(View, GeneralTasksView):
    def get(self, request):
        tasks_temp = Task.objects.filter(is_done=False)
        tasks = tasks_temp.filter(is_archived=False)
        form = AddTaskForm()

        context = {
            'tasks': tasks,
            'form': form,
        }

        return render(request, 'todo/index.html', context)
    
    
class AllTasksView(View, GeneralTasksView):
    def get(self, request):
        tasks = Task.objects.all()
        form = AddTaskForm()

        context = {
            'tasks': tasks,
            'form': form,
        }

        return render(request, 'todo/index.html', context)


class ArchiveTasksView(View):
    def get(self, request):
        tasks = Task.objects.filter(is_archived=True)

        context = {
            'tasks': tasks,
        }

        return render(request, 'todo/index.html', context)

class TaskDetailView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        form = AddTaskFormAdvance(instance=task)

        context = {
            'task': task,
            'form': form,
        }

        return render(request, 'todo/task-detail.html', context)
    
    def post(self, request, id):
        task = Task.objects.get(pk=id)
        form = AddTaskFormAdvance(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('starting-page')
    
class RemoveTaskView(View):
    def get(self, request, id):
        Task.objects.get(pk=id).delete()

        return redirect('starting-page')
    
class CompleteTaskView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        task.is_done = True
        task.save()

        return redirect('starting-page')
    
class MoveToArchiveView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        task.is_archived = True
        task.save()

        return redirect('starting-page')
