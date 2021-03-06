from django.db import models
import uuid
# Create your models here.
class Project(models.Model):
    #owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #featured_image =
    demo_link = models.CharField(max_length=1000,null=True,blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('Up','Up'),
        ('Down','Down'),
    )
    #owner =
    project = models.ForeignKey(Project,on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=50,choices=VOTE_TYPE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):

    name = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name