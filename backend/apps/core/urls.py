from django.urls import include, path
from .views import set_csrf
from apps.accounts import urls as students_urls

urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
]
