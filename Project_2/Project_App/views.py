from django.shortcuts import render, redirect
from .forms import Movie_Regular_Form,Movie_Lib_Form,Model_File_Upload
from .models import Movies, Movie_Lib,UploadFile

# Create your views here.

def regular_form_movies(request):
    if request.method == 'POST':
        form = Movie_Regular_Form(request.POST)
        if form.is_valid():
            title = form.data.get('Title')
            director = form.data.get('Director')
            genre = form.data.get('Genre')
            year = form.data.get('Year')
    
            movie = Movies.objects.create(Title=title, Director=director, Genre=genre, Year=year)
            movie.save()
            
            return movie_details(request)
    else:
        form = Movie_Regular_Form()
        
    return render(request, 'regular_form.html', {'form': form})


def movie_details(request):
    movies = Movies.objects.all()
    return render(request, 'success.html', {'data': movies})


def model_forms_lib(request) :
    form_lib = Movie_Lib_Form()
    if request.method == 'POST' :
        form_lib = Movie_Lib_Form(request.POST)
        if form_lib.is_valid():
            form_lib.save()
            return Lib_details(request)
    return render(request,"model_form.html",{'form_lib' : form_lib})

def Lib_details(request) :
    library = Movie_Lib.objects.all()
    return render(request,'lib_success.html',{'data_lib' : library})

def model_form_file_upload(request) :
    if request.method == 'POST':
        file_form = Model_File_Upload(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
            return file_display(request)
    else:
        file_form = Model_File_Upload()
    return render(request,"file_form.html",{"form":file_form})

def file_display(request) :
    files = UploadFile.objects.all()
    return render(request,"file_list.html",{'files':files})