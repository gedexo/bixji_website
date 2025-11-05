from django import forms
from .models import Contact
from django.forms import widgets


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