from django.contrib import admin
from .models import Contact, Banners    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject",)

@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ( "banner_video",)