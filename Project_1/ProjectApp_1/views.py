from django.shortcuts import render
from .models import Movies,MovieLib
from django.views import View
from django.views.generic import ListView,DetailView

# Create your views here.

def MovieList(request) :
    movies = Movies.objects.all()
    return render(request,'MovieList.html',{'data':movies})

class MovieLib(ListView) :
    model = MovieLib
    template_name = 'LibList.html' 
    context_object_name = 'MovieLibs'

def MovieDetails(request, pk) :
    movies_details = Movies.objects.get(pk = pk)
    context = {
        'movie' : movies_details
    }
    return render(request,'detail.html',context)

class Movie_Det(DetailView):
    model = Movies
    template_name = 'detail_1.html'
    context_object_name = 'movie'