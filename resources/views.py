from django.views.generic import ListView
from .models import Resources
# Create your views here.


# handle request to view resources.html - Johnny
class Resources(ListView):
    """ View all resources """
    template_name = 'resources/resources.html'
    model = Resources
    context_object_name = "resources"
