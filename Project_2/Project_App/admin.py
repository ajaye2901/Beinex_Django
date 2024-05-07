from django.contrib import admin
from .models import Movies, Movie_Lib, UploadFile

# Register your models here.
admin.site.register(Movies)
admin.site.register(Movie_Lib)
admin.site.register(UploadFile)