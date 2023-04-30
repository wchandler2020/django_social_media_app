from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
def projects(request):
    first_name = 'William'
    last_name = 'Chandler'
    project_query = Project.objects.all()
    context = {
        'projects': project_query
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        'project': projectObj
    }
    return render(request, 'projects/single_project.html', context)

def create_project(request):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)

