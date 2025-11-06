from django.contrib import admin
from .models import Contact, Banners, Magazine, Award, Club, Event, BixjiTalk, Team, FAQ, Testimonial

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject",)

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ( "title",)

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "location", "author")
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BixjiTalk)
class BixjiTalkAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")