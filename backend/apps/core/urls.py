from django.urls import include, path
from .views import set_csrf
from apps.work_space import urls as work_space_urls

urlpatterns = [
    path("csrf/", set_csrf, name="csrf"),
    path("work_space/", include(work_space_urls)),

]
