from django.db import models


class WorkSpace(models.Model):
    user_uuid = models.UUIDField(
        default=None,
        editable=False,
        unique=True,
        null=True,
    )

    name = models.CharField(
        max_length=50,
        default=None,
        null=True,
    )


