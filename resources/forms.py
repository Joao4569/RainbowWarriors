from django import forms
from .models import Resources


class ResourceForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Resources
        fields = [
            "title",
            "category",
            "image_preview",
            "description",
            "public_url",
        ]

        labels = {
            "title": "Resource Title",
            "description": "Description",
            "category": "What kind of resource are you posting?",
            "public_url": "Paste the URL of videos/ebooks/news",
            "image_preview": "Resource Image",
        }