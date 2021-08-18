from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
# Create your views here.

# 
def home(request):
    projectsList = Project.objects.all()
    
    context = {'projectsList' : projectsList}
    
        
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    reviews = project.review_set.all()
    context = {'project':project, 'tags': tags, 'reviews':reviews }       
    
    return render(request, 'projects/project.html',context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("form is not valid")
    
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            print("form is not valid")




    context ={'form':form,'project':project}
    return render(request,'projects/project_form.html',context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')


    context ={'project':project}
    return render(request,'projects/delete_project.html',context)
