from django.urls import path

from . import views

app_name = "app_todolist"


urlpatterns = [
    path("todolist/", views.todolistPage, name="todolist"),

]
