from django.db import models
from tinymce.models import HTMLField


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
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    banner_video = models.FileField(upload_to='banners/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    
class Magazine(models.Model):
    title = models.CharField(max_length=200)
    magazine_link = models.URLField(help_text="Link to the magazine PDF (e.g., Google Drive link)")
    image = models.ImageField(upload_to='magazines/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Magazine'
        verbose_name_plural = 'Magazines'

    
class Award(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='awards/')
    description = HTMLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    
class AwardImages(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='award_images')
    image = models.ImageField(upload_to='award_images/')

    def __str__(self):
        return f"Image for {self.award.title}"
    
    class Meta:
        verbose_name = 'Award Image'
        verbose_name_plural = 'Award Images'

    
class Club(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='clubs/')
    description = HTMLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='event_authors/')
    description = HTMLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    
class BixjiTalk(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.URLField(help_text="Link to the Bixji Talk video (e.g., YouTube link)")
    image = models.ImageField(upload_to='bixji_talks/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bixji Talk'
        verbose_name_plural = 'Bixji Talks'

    
class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = HTMLField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials/')
    position = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'