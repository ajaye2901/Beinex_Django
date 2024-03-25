from django.urls import path
from .views import *

urlpatterns = [
    path('jobupdate/',create_job,name='jobupdate'),
    path('joblist/', displayjob, name='joblist'),
    path('edit-job/<int:pk>/', edit_job, name='edit_job'),
    path('delete-job/<int:pk>/', delete_job, name='delete_job'),
    path('job-applicants/<int:job_id>/', job_applicants, name='job_applicants'),
    path('logout/',user_logout,name='logout')
]