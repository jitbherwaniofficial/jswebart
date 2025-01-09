from django import forms

from .models import Subscriber

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Your Email',
                'class': 'form-control',
            })
        }