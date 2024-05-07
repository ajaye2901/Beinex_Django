from django import forms
from .models import CheckoutInfo

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutInfo
        fields = ['full_name', 'address', 'mobile_no']