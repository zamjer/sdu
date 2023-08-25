from django.urls import path

from . import views

app_name = "app_task"


urlpatterns = [
    path("task/", views.taskPage, name="task"),

]
