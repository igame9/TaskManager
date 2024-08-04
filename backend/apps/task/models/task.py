from django.db import models
from apps.desk.models import Desk


class TaskStatus(models.TextChoices):
    READY = 'RD', 'Ready'
    IN_PROGRESS = 'IP', 'In Progress'
    DELAYED = 'DD', 'Delayed'


class Task(models.Model):
    name = models.CharField(
        max_length=500,
        default=None,
        null=True,
    )

    description = models.TextField(
        default=None,
        null=True,
    )

    desk = models.ForeignKey(
        Desk,
        on_delete=models.CASCADE,
        null=False,
        related_name="tasks",
    )

    status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices,
    )
