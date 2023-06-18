from django.contrib import admin

# Import Event model - Johnny
from .models import Resources, Category


# Expose models to admin panel - Debbie

admin.site.register(Resources)
admin.site.register(Category)
