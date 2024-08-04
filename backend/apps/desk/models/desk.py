from django.db import models
from apps.work_space.models import WorkSpace


class Desk(models.Model):

    work_space = models.ForeignKey(
        WorkSpace,
        on_delete=models.CASCADE,
        null=False,
        related_name="desks",
    )

    name = models.CharField(
        max_length=50,
        default=None,
        null=True,
    )
