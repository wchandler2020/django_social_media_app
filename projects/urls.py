from django.urls import path
from django.http import HttpResponse
from .views import projects, project, create_project


urlpatterns = [
    path('', projects, name='projects'),
    path('<str:pk>', project, name='project'),
    path('create-project/', create_project, name='create-project'),
]