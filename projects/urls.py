from django.urls import path
from django.http import HttpResponse
from .views import projects


urlpatterns = [
    path('projects/', projects),
]