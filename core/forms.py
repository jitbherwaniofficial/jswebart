from django import forms
from .models import Contact, JoinUs
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
                'data-action': 'submit',
            }
        )
    )
    class Meta:
        model = Contact
        fields = ['name', 'email','country_code', 'phone_number', 'company_stage', 'help_with', 'message',]
        widgets = {
            'help_with': forms.CheckboxSelectMultiple(choices=[
                ('branding', 'Branding'),
                ('rebranding', 'Rebranding'),
                ('ui_ux', 'UI/UX Design'),
                ('web_dev', 'Web Development'),
                ('digital_marketing', 'Digital Marketing'),
                ('social_media', 'Social Media Marketing'),
                ('packaging_design', 'Packaging Design'),
                ('print_design', 'Print Design'),
            ]),
            'message': forms.Textarea(attrs={'placeholder': 'Your message here..','required':'required'}),
        },
        error_messages = {
            'name': {
                'required': 'Name is required.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'country_code': {
                'required': 'Country code is required.',
                'invalid_choice': 'Select a valid country code.',
            },
            'phone_number': {
                'required': 'Phone number is required.',
            },
            'message': {
                'required': 'Message is required.',
            },
        }


    def clean(self):
        cleaned_data = super().clean()

        # Validate each field

        if not cleaned_data.get('company_stage'):
            self.add_error('company_stage', "Please select the company stage.")
        
        help_with = cleaned_data.get('help_with')
        if not help_with:
            self.add_error('help_with', "You must select at least one option for 'Need Help With'.")
        
        return cleaned_data
    

class JoinUsForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
                'data-action': 'submit',
            }
        )
    )
    class Meta:
        model = JoinUs
        fields = [
            'join_us_name',
            'join_us_email',
            'join_us_country_code',
            'join_us_phone_number',
            'file_upload',
            'position_applying_for',
            'location',
            'join_us_message',
        ]

    def clean_file_upload(self):
        file = self.cleaned_data.get('file_upload')
        if file:
            allowed_types = ['application/pdf', 'image/jpeg', 'image/png', 'image/gif', 'application/msword']
            if file.content_type not in allowed_types:
                raise forms.ValidationError("File type not supported.")
            if file.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size exceeds 5MB limit.")
        return file    