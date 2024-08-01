from django.urls import include, path
from .views import set_csrf
from apps.accounts import urls as accounts_urls
from apps.work_space import urls as work_space_urls
from apps.desk import urls as desk_urls
from apps.task import urls as task_urls

urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
    path("api/accounts/", include(accounts_urls)),
]
