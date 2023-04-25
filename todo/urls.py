from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='starting-page'),
    path('all-tasks', views.AllTasksView.as_view(), name='all-tasks-page'),
    path('archive-tasks', views.ArchiveTasksView.as_view(), name='archived-tasks-page'),
    path('login-required', views.LoginRequiredView.as_view(), name='login-required-page'),
    path('<int:id>', views.TaskDetailView.as_view(), name='task-detail-page'),
    path('complete-task/<int:id>', views.CompleteTaskView.as_view(), name='complete-task-page'),
    path('remove-task/<int:id>', views.RemoveTaskView.as_view(), name='remove-task-page'),
    path('move-to-archive/<int:id>', views.MoveToArchiveView.as_view(), name='move-to-archive-page'),
]
