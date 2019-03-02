from django.db import models


class Task(models.Model):
    # task id
    id = models.AutoField(primary_key=True)
    # task name
    name = models.CharField(max_length=255, null=False)
    # task description
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description}"
