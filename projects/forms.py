from django.db.models import fields
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model= Project
        fields= '__all__'
        exclude= ['demo_link','source_link','vote_total','vote_ratio']
