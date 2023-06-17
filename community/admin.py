from django.contrib import admin
# Import UserProfile model - Johnny
from .models import UserProfile
# Import Event model - Johnny
from .models import Event
# Import Comment model - Johnny
from .models import Comment

# Register your models here.

# Expose models to admin panel - Johnny
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Comment)
