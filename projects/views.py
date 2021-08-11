from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):

    return render(request, 'projects/project.html')

def project(request,id):
    
    return render(request, 'projects/projects.html')
