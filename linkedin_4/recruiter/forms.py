from django import forms
from .models import NewJob

class NewJobForm(forms.ModelForm):
    class Meta:
        model = NewJob
        fields = ['Position', 'Salary', 'Location', 'Job_type', 'Job_requirement', 'Available']