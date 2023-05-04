from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
def projects(request):
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

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, 'projects/project_form.html', context)

def delete_project(request, pk):
    delete_project = Project.objects.get(id=pk)
    if request.method == 'POST':
        delete_project.delete()
        return redirect('projects')
    context = {'delete_project': delete_project}
    return render(request, 'projects/delete_confirmation.html', context)

