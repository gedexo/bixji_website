from django.db import models


class Contact(models.Model):
    ENQUIRY_TYPE = [
        ("general","General"),
        ("collaboration","Collaboration"),
        ("media","Media"),
        ("sponsorship","Sponsorship"),

    ]
    enquiry_type = models.CharField(max_length=180, choices=ENQUIRY_TYPE, default="general")
    name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    
class Banners(models.Model):
    banner_video = models.FileField(upload_to='banners/')

    def __str__(self):
        return f"Banner {self.id}"
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'