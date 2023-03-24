from django.urls import path
from . import views

urlpatterns = [
    path('api/projects', views.ProjectsAPI.as_view()),
    path('api/testprojects', views.TestProjectsAPI.as_view()),
    path('api/logger', views.LoggerAPI.as_view()),
    path('api/testlogger', views.TestLoggerAPI.as_view()),
    path('api/walletmapper/<slug:walletAddress>', views.WalletMapperAPI.as_view())
]