from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from .forms import UpdateUserform, JobApplicationForm
from .forms import UpdateProfile, JobApplication
from recruiter.models import NewJob
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

@login_required(login_url='login/')
def jobseeker_home(request) :
    jobs = NewJob.objects.all()
    return render(request,'jobseeker/homepage.html',{'jobs':jobs})

@login_required(login_url='login/')
def update_profile(request):
    profile_instance = UpdateProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = UpdateUserform(request.POST, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('user_details')
    else:
        form = UpdateUserform(instance=profile_instance)
    return render(request, 'jobseeker/update.html', {'form': form})

@login_required(login_url='login/')
def user_details(request) :
    details = UpdateProfile.objects.filter(user=request.user).first()
    return render(request,'jobseeker/profile.html',{'data':details})

@login_required(login_url='login/')
def apply_job(request, job_id):
    job = get_object_or_404(NewJob, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()

            jobseeker_mail = request.user.email
            jobseeker_subject = f'Application for {job.Position}'
            jobseeker_message = f'You have successfull applied for the {job.Position}.'
            send_mail(jobseeker_subject,jobseeker_message,settings.EMAIL_HOST_USER, [jobseeker_mail])

            recuiter_mail = job.recruiter.email
            recuiter_subject = f'Application for {job.Position}'
            recuiter_message = f'{request.user.username} applied for {job.Position}' 
            send_mail(recuiter_subject,recuiter_message,settings.EMAIL_HOST_USER, [recuiter_mail])

            return render(request,'jobseeker/homepage.html')
    else:
        form = JobApplicationForm()
    return render(request, 'jobseeker/applyjob.html', {'form': form, 'job': job})

def user_logout(request) :
    logout(request)
    return redirect(reverse('login'))