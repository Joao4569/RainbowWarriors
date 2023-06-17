from django.contrib import admin
# Import UserProfile model - Johnny
from .models import UserProfile

# Register your models here.

# Expose model to admin panel - Johnny
admin.site.register(UserProfile)
