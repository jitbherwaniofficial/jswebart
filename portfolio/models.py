from django.db import models
from django.utils.text import slugify

# Create your models here.

from django.db import models

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    # title = models.CharField(max_length=255, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Auto-generate slug from name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Portfolio Categories"

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=700, unique=True, blank=True)
    description = models.TextField()
    categories = models.ManyToManyField(PortfolioCategory, related_name='portfolios')  # Many-to-Many Relationship
    image = models.ImageField(upload_to='portfolio_images/')  # For images if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            max_length = 700
            self.slug = slugify(self.title)[:max_length]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
