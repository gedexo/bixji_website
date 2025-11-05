import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from . import forms
from .models import Banners


def index(request):
    context = {
        "is_index":True,
        "banners": Banners.objects.all(),
    }
    return render(request, 'web/index.html', context)


def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        
        turnstile_response = request.POST.get('cf-turnstile-response')
        data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY, 
            'response': turnstile_response,
        }
        
        captcha_response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid(): 
                data = form.save()

                # WhatsApp Message
                whatsapp_message = (
                    f"Subject: BIXJI New Contact Enquiry%0A%0A"
                    f"Enquiry Type: {data.enquiry_type}%0A"
                    f"Name: {data.name}%0A"
                    f"Email: {data.email}%0A"
                    f"Phone: {data.phone}%0A"
                    f"Subject: {data.subject}%0A"
                    f"Message: {data.message}"
                )
                whatsapp_url = f"https://wa.me/+919847520679?text={whatsapp_message}" 

                response_data = {
                    "status": "true",
                    "title": "Successfully Submitted",
                    "message": "Message successfully sent",
                    "whatsapp_url": whatsapp_url,  
                }
                return JsonResponse(response_data)
            else:
                response_data = {
                    "status": "false",
                    "title": "Form validation error",
                    "message": "Please ensure all fields are filled out correctly."
                }
                return JsonResponse(response_data)

        else:
            response_data = {
                "status": "false",
                "title": "CAPTCHA verification failed",
                "message": "Please complete the CAPTCHA correctly."
            }
            return JsonResponse(response_data)

    else:
        form = forms.ContactForm()
        context = {
            "is_contact": True,
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
        }
    return render(request, "web/contact.html", context)