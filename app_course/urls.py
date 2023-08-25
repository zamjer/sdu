from django.urls import path

from . import views

app_name = "app_course"


urlpatterns = [
    path("course/", views.coursePage, name="course"),

]
