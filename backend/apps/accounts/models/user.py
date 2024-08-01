from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from apps.accounts.services import UserManager


class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        primary_key=True,
    )

    email = models.EmailField("email address", unique=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
