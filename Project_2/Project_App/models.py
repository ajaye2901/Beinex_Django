from django.db import models

# Create your models here.

class Movies(models.Model) :
    Title = models.CharField(max_length = 100)
    Director = models.CharField(max_length = 100)
    Genre = models.CharField(max_length = 100)
    Year = models.IntegerField()

class Movie_Lib(models.Model) :
    Name = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    Lib_ID = models.IntegerField()

class UploadFile(models.Model) :
    Filename = models.CharField(max_length = 200)
    doc = models.FileField(upload_to='uploads/')
