from django.db import models
# User object needed for UserProfile model - Johnny
from django.contrib.auth.models import User
# Import the post_save signal - Johnny
from django.db.models.signals import post_save
# Import receiver decorator from Django built-in signals framework - Johnny
from django.dispatch import receiver


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
    default_country = models.CharField(max_length=40, null=False)

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
