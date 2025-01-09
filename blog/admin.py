from django.contrib import admin
from .models import BlogCategory, Blog, Subscriber
from .models import ContentSection


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ContentSectionInline(admin.TabularInline):
    model = ContentSection
    extra = 0  # Number of empty section forms shown by default
    fields = ('heading', 'content', 'order')
    ordering = ('order',)
    readonly_fields = ('page',)  # Optionally show the associated blog page


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'category__name',)
    list_filter = ('created_at',)
    inlines = [ContentSectionInline]

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
