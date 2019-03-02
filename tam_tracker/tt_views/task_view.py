from rest_framework import generics
from tam_tracker.tt_models.task import Task
from tam_tracker.tt_serializers.task_serializer import TaskSerializer


class ListTaskView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer