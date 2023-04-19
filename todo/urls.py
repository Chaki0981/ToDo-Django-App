from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='starting-page'),
    path('<int:id>', views.TaskDetailView.as_view(), name='task-detail-page'),
    path('complete-task/<int:id>', views.CompleteTaskView.as_view(), name='complete-task-page'),
    path('remove-task/<int:id>', views.RemoveTaskView.as_view(), name='remove-task-page'),
]
