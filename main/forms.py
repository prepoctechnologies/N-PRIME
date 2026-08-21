from django import forms
from .models import ConsultationEnquiry, CallbackRequest, ContactMessage, SERVICE_CHOICES


class ConsultationForm(forms.ModelForm):
    service = forms.ChoiceField(
        choices=[('', '— Select a Service —')] + list(SERVICE_CHOICES),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = ConsultationEnquiry
        fields = ['full_name', 'phone', 'email', 'service', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-0000'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your requirements...',
                'rows': 4
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'service': 'Service Required',
            'message': 'Message',
        }


class CallbackForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'phone', 'preferred_time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'preferred_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Monday 10am–12pm'
            }),
        }
        labels = {
            'name': 'Your Name',
            'phone': 'Phone Number',
            'preferred_time': 'Preferred Callback Time',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number (optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'rows': 5
            }),
        }
