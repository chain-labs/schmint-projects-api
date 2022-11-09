from django.urls import path
from . import views

urlpatterns = [
    path('api/projects', views.ProjectsAPI.as_view()),
    path('api/testprojects', views.TestProjectsAPI.as_view())
]