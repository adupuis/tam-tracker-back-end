from django.urls import path
from tam_tracker.tt_views.task_view import ListTaskView


urlpatterns = [
    path('task/', ListTaskView.as_view(), name="task-all")
]