from django.db import models
# User object needed for UserProfile model - Johnny
from django.contrib.auth.models import User
# Import the post_save signal - Johnny
from django.db.models.signals import post_save
# Import receiver decorator from Django built-in signals framework - Johnny
from django.dispatch import receiver
# Import countryfield - Johnny
from django_countries.fields import CountryField
# Import for models to store media on Cloudinary
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Date and time field for models
from django.utils import timezone

class Resources(models.Model):
    """
    A user profile model for maintaining default
    user information and history - Johnny
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Compulsory field
    title = models.CharField(max_length=200, null=False)

    # Compulsory field
    category = models.IntegerField(null=False)

    # Compulsory field
    image_preview = models.CharField(max_length=80, null=True,
                                               blank=True)

    # Compulsory field
    description = models.CharField(max_length=40, null=False)

    # Compulsory field
    created_on = models.DateTimeField(null=True, blank=True)

    # Compulsory field
    updated_on = models.DateTimeField(null=True, blank=True)

    # Compulsory field
    public_url = models.URLField(null=False)

    # Compulsory field
    submitted_by = models.CharField(max_length=30, null=False)

    # Compulsory field
    approved = models.BooleanField(null=False)

    # In Django models, this is used to define how an instance of the model
    # should be represented as a string.
    def __str__(self):
        return self.user.username