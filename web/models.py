from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy


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
    meta_title = models.CharField(max_length=180, blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=180, blank=True, null=True)
    image = models.ImageField(upload_to='awards/')
    description = HTMLField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("web:award_detail", kwargs={"slug": self.slug}) 
    
    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    
class AwardGallery(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE, related_name='award_images')
    image = models.ImageField(upload_to='award_images/')

    def __str__(self):
        return f"Image for {self.award.title}"
    
    class Meta:
        verbose_name = 'Award Gallery'
        verbose_name_plural = 'Award Galleries'


class AwardNomination(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Award Nomination'
        verbose_name_plural = 'Award Nominations'

    
class Club(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=180, blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=180, blank=True, null=True)
    image = models.ImageField(upload_to='clubs/')
    description = HTMLField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("web:club_detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    
class ClubRegistration(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=180, blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.CharField(max_length=180, blank=True, null=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='event_authors/')
    description = HTMLField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("web:event_detail", kwargs={"slug": self.slug})
    
    def get_event_images(self):
        return EventGallery.objects.filter(event=self)
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    sloat = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registration for {self.event.title} by {self.name}"
    
    class Meta:
        verbose_name = 'Event Registration'
        verbose_name_plural = 'Event Registrations'

    
class EventGallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='event_galleries/')

    def __str__(self):
        return f"Gallery for {self.event.title}"
    
    class Meta:
        verbose_name = 'Event Gallery'
        verbose_name_plural = 'Event Galleries'

    
class BixjiTalk(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.URLField(help_text="Link to the Bixji Talk video (e.g., YouTube link)")
    image = models.ImageField(upload_to='bixji_talks/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Bixji Talk'
        verbose_name_plural = 'Bixji Talks'


class BixjiTalkEnquiry(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)   
    bio = models.TextField()    
    social_link = models.TextField()
    short_video_link = models.URLField(help_text="Link to the short video (e.g., YouTube, Instagram link)")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Bixji Talk Enquiry'
        verbose_name_plural = 'Bixji Talk Enquiries'

    
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
    answer = models.TextField()

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

    
class Meta(models.Model):
    PAGES = (
        ('home', 'Home'),
        ('about', 'About'),
        ('bixji_talks', 'Bixji Talks'),
        ('magazines', 'Magazines'),
        ('awards', 'Awards'),
        ('awards_gallery', 'Awards Gallery'),
        ('clubs', 'Clubs'),
        ('events', 'Events'),
        ('event_gallery', 'Event Gallery'),
        ('contact', 'Contact'),
    )
    page = models.CharField(max_length=180, choices=PAGES)
    meta_title = models.CharField(max_length=180)
    meta_keywords = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=180)
    canonical_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="meta/", blank=True, null=True)
    
    def __str__(self):
        return self.meta_title
    
    class Meta:
        ordering = ["-id"]
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
