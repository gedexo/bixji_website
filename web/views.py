import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from . import forms
from .models import Banners, Magazine, Award, AwardGallery, Club, Event, EventGallery, BixjiTalk, Meta, Testimonial, FAQ, Team


def index(request):
    context = {
        "is_index":True,
        "banners": Banners.objects.all(),
        "magazines": Magazine.objects.all()[:6],
        "awards": Award.objects.all()[:3],
        "clubs": Club.objects.all()[:3],
        "events": Event.objects.all()[:3],
        "bixji_talks": BixjiTalk.objects.all(),
        "meta" : Meta.objects.filter(page='home').first(),
    }
    return render(request, 'web/index.html', context)


def about(request):
    context = {
        "is_about": True,
        "testimonials": Testimonial.objects.all(),
        "faqs": FAQ.objects.all(),
        "teams": Team.objects.all(),
        "meta" : Meta.objects.filter(page='about').first(),
    }
    return render(request, "web/about.html", context)


def bixji_talks(request):
    if request.method == "POST":
        form = forms.BixjiTalkEnquiryForm(request.POST)
        
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
                    f"Subject: New Bixji Talk Enquiry%0A%0A"
                    f"Name: {data.name}%0A"
                    f"Profession: {data.profession}%0A"
                    f"Bio: {data.bio}%0A"
                    f"Social Link: {data.social_link}%0A"
                    f"short_video_link: {data.short_video_link}"
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
        form = forms.BixjiTalkEnquiryForm()
        context = {
            "is_bixji_talks": True,
            "bixji_talks": BixjiTalk.objects.all(),
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
            "meta" : Meta.objects.filter(page='bixji_talks').first(),

        }
    return render(request, "web/bixji_talks.html", context)


def magazines(request):
    context = {
        "is_magazines": True,
        "magazines": Magazine.objects.all(),
        "meta" : Meta.objects.filter(page='magazines').first(),
    }
    return render(request, "web/magazines.html", context)


def awards(request):
    context = {
        "is_awards": True,
        "awards": Award.objects.all(),
        "meta" : Meta.objects.filter(page='awards').first(),
    }
    return render(request, "web/awards.html", context)


def award_detail(request, slug):
    award = get_object_or_404(Award, slug=slug)
    if request.method == "POST":
        form = forms.AwardNominationForm(request.POST)
        
        turnstile_response = request.POST.get('cf-turnstile-response')
        data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY, 
            'response': turnstile_response,
        }
        
        captcha_response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid(): 
                data = form.save(commit=False) 
                data.award = award 
                data.save()  

                # WhatsApp Message
                whatsapp_message = (
                    f"Subject: BIXJI {data.award.title} Enquiry%0A%0A"
                    f"Name: {data.name}%0A"
                    f"Email: {data.email}%0A"
                    f"Phone: {data.phone}%0A"
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
        form = forms.AwardNominationForm()
        context = {
            "is_award_detail": True,
            "award": award,
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
        }
    return render(request, "web/awards-detail.html", context)


def award_gallery(request):
    awards = Award.objects.all()
    award_galleries = AwardGallery.objects.select_related('award').all()

    context = {
        "is_awards": True,
        "is_award_gallery": True,
        "awards": awards,
        "award_galleries": award_galleries,
        "meta" : Meta.objects.filter(page='awards_gallery').first(),
    }
    return render(request, "web/award-gallery.html", context)


def clubs(request):
    context = {
        "is_clubs": True,
        "clubs": Club.objects.all(),
        "meta" : Meta.objects.filter(page='clubs').first(),
    }
    return render(request, "web/clubs.html", context)


def club_detail(request, slug): 
    club = get_object_or_404(Club, slug=slug)   
    other_clubs = Club.objects.exclude(slug=slug)
    if request.method == "POST":
        form = forms.ClubRegistrationForm(request.POST)
        
        turnstile_response = request.POST.get('cf-turnstile-response')
        data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY, 
            'response': turnstile_response,
        }
        
        captcha_response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid(): 
                data = form.save(commit=False) 
                data.club = club 
                data.save()  

                # WhatsApp Message
                whatsapp_message = (
                    f"Subject: BIXJI {data.club.name} Enquiry%0A%0A"
                    f"Name: {data.name}%0A"
                    f"Email: {data.email}%0A"
                    f"Phone: {data.phone}%0A"
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
        form = forms.ClubRegistrationForm()
        context = {
            "is_club_detail": True,
            "club": club,
            "other_clubs": other_clubs,
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
        }
    return render(request, "web/club_detail.html", context) 


def events(request):
    context = {
        "is_events": True,
        "events": Event.objects.all(),
        "meta" : Meta.objects.filter(page='events').first(),
    }
    return render(request, "web/events.html", context)


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug) 
    if request.method == "POST":
        form = forms.EventRegistrationForm(request.POST)
        
        turnstile_response = request.POST.get('cf-turnstile-response')
        data = {
            'secret': settings.CLOUDLFAIR_TURNSTILE_PRIVATE_KEY, 
            'response': turnstile_response,
        }
        
        captcha_response = requests.post('https://challenges.cloudflare.com/turnstile/v0/siteverify', data=data)
        captcha_result = captcha_response.json()

        if captcha_result.get('success'):
            if form.is_valid(): 
                data = form.save(commit=False) 
                data.event = event 
                data.save()  

                # WhatsApp Message
                whatsapp_message = (
                    f"Subject: BIXJI {data.event.title} Enquiry%0A%0A"
                    f"Name: {data.name}%0A"
                    f"Email: {data.email}%0A"
                    f"Phone: {data.phone}%0A"
                    f"Sloat: {data.sloat}%0A"
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
        form = forms.EventRegistrationForm()
        context = {
            "is_event_detail": True,
            "event": event,
            "form": form,
            "turnstile_site_key": settings.CLOUDLFAIR_TURNSTILE_PUBLIC_KEY,
        }
    return render(request, "web/events-details.html", context)


def event_gallery(request):
    events = Event.objects.all()
    event_galleries = EventGallery.objects.select_related('event').all()

    context = {
        "is_events": True,
        "is_event_gallery": True,
        "events": events,
        "event_galleries": event_galleries,
        "meta" : Meta.objects.filter(page='event_gallery').first(),
    }
    return render(request, "web/event-gallery.html", context)


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
            "meta" : Meta.objects.filter(page='contact').first(),
        }
    return render(request, "web/contact.html", context)