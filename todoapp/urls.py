from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, complete_task
# emailsend

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:task_id>/complete/', complete_task, name='complete_task'),
    # path('task/sendmail', emailsend, name='send-email'),
]
