from django.urls import path
from .views import *

urlpatterns = [
    path('update',update_profile,name='update_profile'),
    path('profile',user_details,name='user_details'),
    path('applyjob/<int:job_id>/', apply_job,name='apply_job'),
    path('logout/',user_logout,name='logout')
]