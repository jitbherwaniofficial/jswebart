from django.contrib import admin

# Register your models here.
from .models import Contact, JoinUs


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')

@admin.register(JoinUs)
class JoinAdmin(admin.ModelAdmin):
    list_display = ('join_us_name', 'join_us_email')