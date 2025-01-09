from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from math import ceil


# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = 700
            self.slug = slugify(self.name)[:max_length]  # Auto-generate slug from name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=700, unique=True, blank=True)
    categories = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,default="")  # Many-to-Many Relationship
    image = models.ImageField(upload_to='blogs_images/')  # For images if needed
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = 700
            self.slug = slugify(self.title)[:max_length]
        super().save(*args, **kwargs)

    def get_total_read_time(self):
        sections = self.sections.all()  # Related name `sections` from ContentSection
        total_word_count = sum(len(section.content.split()) for section in sections)
        words_per_minute = 200
        read_time_minutes = ceil(total_word_count / words_per_minute)
        return read_time_minutes


    def __str__(self):
        return self.title
    



# Sections on the right side of the page
class ContentSection(models.Model):
    page = models.ForeignKey(Blog, related_name='sections', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, help_text="Section heading for table of contents",blank=True,default="")
    content = models.TextField(help_text="HTML content for the section", blank=True,default="")
    order = models.PositiveIntegerField(default=0, help_text="Order of the section on the page")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.page.title} - {self.heading}"



class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email Address")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
