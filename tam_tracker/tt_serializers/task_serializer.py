
from rest_framework import serializers
from tam_tracker.tt_models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id","name", "description")