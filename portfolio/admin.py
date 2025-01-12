from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Portfolio, PortfolioCategory

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('categories',)  # Provides a better UI for ManyToMany fields
    class Media:
        js = ('https://widget.cloudinary.com/v2.0/global/all.js',)

@admin.register(PortfolioCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

