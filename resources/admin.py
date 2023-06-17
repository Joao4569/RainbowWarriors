from django.contrib import admin

# Import Event model - Johnny
from .models import Resources


# Expose models to admin panel - Debbie

admin.site.register(Resources)
