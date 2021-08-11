from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectsList =[
    {'id' : '1',
    'title' : 'Ecommerce website',
    'description' : 'fully functional shopping website',
    'topRated' : True
    },
    {'id' : '2',
    'title' : 'Todo List',
    'description' : 'A personal website to listout things',
    'topRated' : False

    },
    {'id' : '3',
    'title' : 'Social media',
    'description' : 'Social media website for developers',
    'topRated' : True

    }

]
def home(request):
    name = "Rari Raj C"
    context = {'name':name, 'projectList' : projectsList}

    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObject = None

    for item in projectsList:
        if item['id']== str(pk) :
            projectObject = item
            
    context = {'project':projectObject}        
    
    return render(request, 'projects/project.html',context)
