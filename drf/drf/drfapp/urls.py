from django.urls import path
from .views import UserCreate, UserDetails, UserRetrieveAPIView
 
urlpatterns = [
    path('usercreate/', UserCreate.as_view(), name='usercreate'),
    path('userdetails/<int:pk>/', UserDetails.as_view(), name='userdetails'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='userretrieve'),
]

