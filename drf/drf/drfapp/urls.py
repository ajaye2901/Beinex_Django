from django.urls import path
from .views import UserCreate, UserDetails, UserRetrieveAPIView, SnippetCreate, SnippetView, SnippetUpdate, SnippetDelete, SnippetBulkDelete
 
urlpatterns = [
    path('usercreate/', UserCreate.as_view(), name='usercreate'),
    path('userdetails/<int:pk>/', UserDetails.as_view(), name='userdetails'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='userretrieve'),
    path('snippet/', SnippetCreate.as_view(), name='snippet'),
    path('snippetview/<int:pk>', SnippetView.as_view(), name='snippetview'),
    path('snippetupdate/<int:pk>', SnippetUpdate.as_view(), name='snippetupdate'),
    path('snippetdelete/<int:pk>', SnippetDelete.as_view(), name='snippetdelete'),
    path('snippetbulkdelete/', SnippetBulkDelete.as_view(), name='snippetbulkdelete'),
]

