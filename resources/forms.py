from django import forms
from .models import Resources


class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = '__all__'

    image_preview = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
