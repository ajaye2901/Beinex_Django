from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import account,user_logout, otp_verification
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account',account,name='account'),
    path('logout',user_logout,name='logout'),
    path('otp-verification/',otp_verification, name='otp_verification'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
