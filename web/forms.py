from django import forms
from django.forms import widgets
from .models import Contact, EventRegistration, ClubRegistration, AwardNomination, BixjiTalkEnquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "enquiry_type": widgets.Select(attrs={"class": "required form-control"}),
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Full Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Phone Number"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Subject"}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
        }

    
class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        exclude = ("timestamp", "event")
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Full Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Phone Number"}),
            "sloat": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Select a Slot"}),
        }

    
class ClubRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClubRegistration
        exclude = ("timestamp", "club")
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Full Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Phone Number"}),
        }

    
class AwardNominationForm(forms.ModelForm):
    class Meta:
        model = AwardNomination
        exclude = ("timestamp", "award")
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Full Name"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Phone Number"}),
        }

    

class BixjiTalkEnquiryForm(forms.ModelForm):
    class Meta:
        model = BixjiTalkEnquiry
        fields = ['name', 'profession', 'bio', 'social_link', 'short_video_link']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Entrepreneur, Artist, Social Leader',
                'required': True
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us your story...',
                'rows': 4,
                'required': True
            }),
            'social_link': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Instagram: https://...\nLinkedIn: https://...',
                'rows': 3,
                'required': True
            }),
            'short_video_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://youtube.com/... or https://instagram.com/...',
                'required': True
            }),
        }