from django import forms
from .models import Movies ,Movie_Lib,UploadFile

class Movie_Regular_Form (forms.Form) :
    Title = forms.CharField(max_length = 100)
    Director = forms.CharField(max_length = 100)
    Genre = forms.CharField(max_length = 100)
    Year = forms.IntegerField()


class Movie_Lib_Form(forms.ModelForm) :
    class Meta:
        model = Movie_Lib
        fields = "__all__"

class Model_File_Upload(forms.ModelForm) :
    class Meta:
        model = UploadFile
        fields = ['Filename','doc']