from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# projectsList =[
#     {'id' : '1',
#     'title' : 'Ecommerce website',
#     'description' : 'fully functional shopping website',
#     'topRated' : True
#     },
#     {'id' : '2',
#     'title' : 'Todo List',
#     'description' : 'A personal website to listout things',
#     'topRated' : False

#     },
#     {'id' : '3',
#     'title' : 'Social media',
#     'description' : 'Social media website for developers',
#     'topRated' : True

#     }

# ]
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
