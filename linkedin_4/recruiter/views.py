from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from .forms import NewJobForm
from .models import NewJob
from jobseeker.models import JobApplication

# Create your views here.

@login_required(login_url='login/')
def recruiter_home(request):
    return render(request,'recruiter/homepage.html')

@login_required(login_url='login/')
def create_job(request):
    if request.method == 'POST':
        form = NewJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            return redirect('joblist')
    else:
        form = NewJobForm()
    return render(request, 'recruiter/jobupdate.html', {'form': form})

@login_required(login_url='login/')
def displayjob(request) :
    jobs = NewJob.objects.filter(recruiter=request.user)
    return render(request,'recruiter/joblist.html',{'jobs':jobs})

@login_required(login_url='login/')
def edit_job(request, pk):
    job = get_object_or_404(NewJob, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        form = NewJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('joblist')
    else:
        form = NewJobForm(instance=job)
    return render(request, 'recruiter/jobupdate.html', {'form': form})

@login_required(login_url='login/')
def delete_job(request, pk):
    job = get_object_or_404(NewJob, pk=pk, recruiter=request.user)
    job.delete()
    return redirect('joblist')

@login_required(login_url='login/')
def job_applicants(request, job_id):
    job = get_object_or_404(NewJob, id=job_id, recruiter=request.user)
    applicants = JobApplication.objects.filter(job=job)
    return render(request, 'recruiter/job_applicants.html', {'applicants': applicants, 'job': job})

def user_logout(request) :
    logout(request)
    return redirect(reverse('login'))