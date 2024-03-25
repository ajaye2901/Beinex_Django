from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserLinkedin

class SignupForm(UserCreationForm) :
    email = forms.EmailField(max_length=100)
    user_type = forms.ChoiceField(choices= UserLinkedin.USER_TYPE_CHOICES, label='Select User Type')

    class Meta :
        model = UserLinkedin
        fields = ('username', 'email', 'password1', 'password2', 'user_type')