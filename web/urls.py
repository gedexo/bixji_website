from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("bixji-talks/", views.bixji_talks, name="bixji_talks"),
    path("magazines/", views.magazines, name="magazines"),
    path("awards/", views.awards, name="awards"),
    path("clubs/", views.clubs, name="clubs"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact")
]