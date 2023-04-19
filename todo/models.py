from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    due_to = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f'Task {self.id}'
