from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('movielist/',MovieList),                       # to show movie list
    path('liblist/',MovieLib.as_view()),                # to show library details
    path('movie/<int:pk>/',MovieDetails),               # to show a movie from the movie list (used function in views)
    path('moviedetail/<int:pk>/',Movie_Det.as_view()),  # to show a movie from the movie list (used Class and detailview in views)
]