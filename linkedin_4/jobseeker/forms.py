from django import forms
from .models import *

class UpdateUserform(forms.ModelForm) :
    class Meta:
        model = UpdateProfile
        fields = ['Contact_no', 'Location', 'Education', 'Skills']

class JobApplicationForm(forms.ModelForm) :
    class Meta :
        model = JobApplication
        fields = ['Fullname','Email','ContactNo','Qualification','Skills','Coverletter','Resume']


    