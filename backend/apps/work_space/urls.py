from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.TestView.as_view(), name="test"),
    path("action/", views.WorkSpaceView.as_view(), name="work_space"),
]
