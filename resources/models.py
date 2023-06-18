from django.db import models
# User object needed for UserProfile model - Johnny
from django.contrib.auth.models import User
# Import the post_save signal - Johnny
from django.db.models.signals import post_save
# Import receiver decorator from Django built-in signals framework - Johnny
from django.dispatch import receiver
# Import for models to store media on Cloudinary
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Date and time field for models
from django.utils import timezone


class Resources(models.Model):
    """
    A model for storing resource information
    """
    # Compulsory field
    title = models.CharField(max_length=200, null=False, blank=False)

    # Non Compulsory field
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)

    # Image field - Non Compulsory
    image_preview = models.ImageField(storage=RawMediaCloudinaryStorage(),
                                      verbose_name='image', null=True,
                                      blank=True)

    # Compulsory description field
    description = models.CharField(max_length=200, null=False, blank=False)

    # This field will record the date and time of the original instance
    created_on = models.DateTimeField(auto_now_add=True)

    # This field will record the date and time, everytime the instance is
    # updated
    updated_on = models.DateTimeField(auto_now=True)

    # like_qty???

    # Compulsory field
    public_url = models.URLField(null=False)

    # Compulsory field
    submitted_by = models.OneToOneField(User, on_delete=models.CASCADE)

    # Compulsory field
    approved = models.BooleanField(default=False)

    # In Django models, this is used to define how an instance of the model
    # should be represented as a string.
    def __str__(self):
        return self.user.username


class Category(models.Model):
    """This model contains each resource category and
    it's related attributes and model methods"""

    class Meta:
        """This model meta class will display the correct spelling of
        the plural of category, django just adds a single s to the end
        of the word, which is incorrect in this case"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """This string model method will take the categoy object itself
        and return its name"""

        return self.name

    def get_friendly_name(self):
        """This model method will take the category itself and
        return it's friendly name"""

        return self.friendly_name
