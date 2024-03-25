from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm
from . models import *
from jobseeker.views import *
from recruiter.views import *

# Create your views here.

def signup(request) :
    if request.method == 'POST' :
        form = SignupForm(request.POST)
        if form.is_valid() :
            form.save()
            return render(request,'login.html')
    else :
        form = SignupForm()
    return render(request, 'register.html', {'form':form})

def userlogin(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'JOB_SEEKER':
                return jobseeker_home(request)
            else:
                return recruiter_home(request)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')