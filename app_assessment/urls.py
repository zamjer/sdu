from django.urls import path

from . import views

app_name = "app_assessment"


urlpatterns = [
    path("assessment/", views.assessmentPage, name="assessment"),

]
