from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_text', 'created_at', 'due_to', 'user','is_done')

admin.site.register(Task, TaskAdmin)