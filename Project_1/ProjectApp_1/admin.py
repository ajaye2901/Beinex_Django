from django.contrib import admin
from .models import Movies, MovieLib

# Register your models here.

admin.site.register(Movies)
admin.site.register(MovieLib)