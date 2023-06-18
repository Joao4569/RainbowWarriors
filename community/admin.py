from django.contrib import admin
# Import models - Johnny
from .models import UserProfile, Event, Comment


# Register your models here.

# Expose models to admin panel - Johnny
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Comment)
