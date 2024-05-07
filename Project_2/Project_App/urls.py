from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('regular_form/',regular_form_movies),
    path('success/',movie_details),
    path('model_form/',model_forms_lib),
    path('lib_success/',Lib_details),
    path('file_form/',model_form_file_upload),
    path('file_list/',file_display)
]