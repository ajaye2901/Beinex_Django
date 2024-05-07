from django.db import models
from linkedin_user.models import UserLinkedin

# Create your models here.
class NewJob(models.Model):
    Position = models.CharField(max_length=100)
    Salary = models.PositiveIntegerField()
    Location = models.CharField(max_length=100)
    Job_type = models.CharField(max_length=20)
    Job_requirement = models.TextField()
    Available = models.BooleanField()
    recruiter = models.ForeignKey(UserLinkedin, on_delete=models.CASCADE, related_name='jobs_posted')