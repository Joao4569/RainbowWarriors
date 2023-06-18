from django.views.generic import (
    CreateView, ListView,
    DeleteView, UpdateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from .forms import ResourceForm
from .models import Resources
# Create your views here.


# handle request to view resources.html - Johnny
class Resources(ListView):
    """ View all resources """
    template_name = 'resources/resources.html'
    model = Resources
    context_object_name = "resources"


class Add_Resource(LoginRequiredMixin, CreateView):
    """Add resource view"""

    template_name = "resources/add_resource.html"
    model = Resources
    form_class = ResourceForm
    success_url = "/resources/"

    def form_valid(self, form):
        form.instance.submitted_by = self.request.user
        return super(Add_Resource, self).form_valid(form)


class Update_Resource(LoginRequiredMixin, 
                      UserPassesTestMixin, 
                      UpdateView):
    """Edit a resource"""
    template_name = 'resources/edit_resource.html'
    model = Resources
    form_class = ResourceForm
    success_url = '/resources/'
    
    def test_func(self):
        # unsolved bug lying here
        return self.request.user == self.get_object().submitted_by