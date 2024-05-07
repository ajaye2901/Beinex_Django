from django.db import models
from linkedin_user.models import UserLinkedin
from django.contrib.auth.models import User
from recruiter.models import NewJob

# Create your models here.

class UpdateProfile(models.Model):
    user = models.OneToOneField(UserLinkedin, on_delete=models.CASCADE, related_name='profile')
    Contact_no = models.CharField(max_length=10)
    Location = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
    Skills = models.CharField(max_length=200)

class JobApplication(models.Model) :
    job = models.ForeignKey(NewJob, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserLinkedin, on_delete=models.CASCADE, related_name='applications')
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField()
    ContactNo = models.PositiveIntegerField()
    Qualification = models.CharField(max_length=100)
    Skills = models.CharField(max_length = 500)
    Coverletter = models.TextField()
    Resume = models.FileField(upload_to='uploads/')