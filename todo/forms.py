from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_text']

class AddTaskFormAdvance(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_text', 'due_to', 'is_done']