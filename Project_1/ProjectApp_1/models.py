from django.db import models

# Create your models here.
class Movies(models.Model) :
    Title = models.CharField(max_length = 100)
    Director = models.CharField(max_length = 100)
    Genre = models.CharField(max_length = 50)
    Release_year = models.IntegerField()

class MovieLib(models.Model) :
    Name = models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
    Lib_ID = models.IntegerField(default = 0)

