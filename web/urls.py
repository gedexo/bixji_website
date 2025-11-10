from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("bixji-talks/", views.bixji_talks, name="bixji_talks"),
    path("magazines/", views.magazines, name="magazines"),
    path("awards/", views.awards, name="awards"),
    path("award-detail/<slug:slug>/", views.award_detail, name="award_detail"),
    path("awards-gallery/", views.award_gallery, name="awards_gallery"),
    path("clubs/", views.clubs, name="clubs"),
    path('club/<slug:slug>/', views.club_detail, name='club_detail'),
    path("events/", views.events, name="events"),
    path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path("event-gallery/", views.event_gallery, name="event_gallery"),
    path("contact/", views.contact, name="contact")
]