from django.contrib import admin
from .models import Contact, Banners, Magazine, Award, AwardNomination, AwardGallery, Club, Event, EventRegistration, EventGallery, BixjiTalk, BixjiTalkEnquiry, Team, FAQ, Testimonial

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

@admin.register(AwardNomination)
class AwardNominationAdmin(admin.ModelAdmin):
    list_display = ("award", "name", "email", "phone", "timestamp")

@admin.register(AwardGallery)
class AwardGalleryAdmin(admin.ModelAdmin):
    list_display = ("award", "image")   

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {'slug': ('name',)}

class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date_time", "location", "author")
    prepopulated_fields = {'slug': ('title',)}
    inlines = [EventGalleryInline]

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("event", "name", "email", "phone", "sloat", "timestamp")

@admin.register(BixjiTalk)
class BixjiTalkAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(BixjiTalkEnquiry)
class BixjiTalkEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "profession")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")