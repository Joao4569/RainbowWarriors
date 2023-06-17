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


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    user information and history - Johnny
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Compulsory field
    default_phone_number = models.CharField(max_length=30, null=False)

    # Compulsory field
    default_street_address1 = models.CharField(max_length=80, null=False)

    # Not compulsory
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)

    # Compulsory field
    default_town_or_city = models.CharField(max_length=40, null=False)

    # Not compulsory
    default_county = models.CharField(max_length=80, null=True, blank=True)

    # Compulsory field
    default_postcode = models.CharField(max_length=20, null=False)

    # Compulsory field
    default_country = CountryField(null=False)

    # In Django models, this is used to define how an instance of the model
    # should be represented as a string.
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile.
    This is a signal receiver function that is called whenever a User instance
    is saved. It creates or updates the corresponding UserProfile instance for
    the saved User. -Johnny
    """

    # If a new user then create the user
    if created:
        UserProfile.objects.create(user=instance)

    # Existing users: just save the profile
    instance.userprofile.save()


class Event(models.Model):
    """
    An event model for storing event information - Johnny
    """
    # Compulsory field
    title = models.CharField(max_length=200, null=False, blank=False)

    # Foreign key to Django User model
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               editable=False)

    # Image field - Non Compulsory
    feat_image = models.ImageField(storage=RawMediaCloudinaryStorage(),
                                   verbose_name='image', null=True, blank=True)

    # Approval field preset to false
    approved = models.BooleanField(default=False)

    # Compulsory description field
    description = models.CharField(max_length=200, null=False, blank=False)

    # This field will record the date and time of the original instance
    created_on = models.DateTimeField(auto_now_add=True)

    # This field will record the date and time, everytime the instance is
    # updated
    updated_on = models.DateTimeField(auto_now=True)

    # Johnny - Not sure what this field is supposed to do
    # join_qty = ????????

    # Compulsory scheduled time and date
    scheduled_on = models.DateTimeField(null=False, blank=False)

    # Compulsory field
    country = CountryField(null=False)

    # Compulsory field
    city = models.CharField(max_length=40, null=False)

    # Compulsory field
    address = models.CharField(max_length=80, null=False)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Comment(models.Model):
    """
    A model for storing comments for events - Johnny
    """
    # Foreign key to Event model
    event = models.ForeignKey(Event, editable=False, on_delete=models.CASCADE)

    # Foreign key to Django User model
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)

    # Foreign key to Django User model
    author_email = models.EmailField()

    # Compulsory field
    title = models.CharField(max_length=200, null=False, blank=False)

    # Compulsory field
    body = models.CharField(max_length=500, null=False, blank=False)

    # This field will record the date and time of the original instance
    created_on = models.DateTimeField(auto_now_add=True)

    # Approval field preset to false
    approved = models.BooleanField(default=False)
