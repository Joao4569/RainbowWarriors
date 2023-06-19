from django.views.generic import (
    CreateView, ListView,
    DeleteView, UpdateView,
    TemplateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.db.models.query import QuerySet
from django.db.models import Q

from .forms import ResourceForm
from .models import Resources
# Create your views here.


# handle request to view resources.html - Johnny
class Resources(ListView):
    """ View all resources """
    template_name = 'resources/resources.html'
    model = Resources
    context_object_name = "resources"
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            resources = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )
        else:
            resources = self.model.objects.all()
        return resources


class Add_Resource(LoginRequiredMixin, CreateView):
    """Add resource view"""

    template_name = "resources/add_resource.html"
    model = Resources
    form_class = ResourceForm
    success_url = "/resources/"

    def form_valid(self, form):
        form.instance.user = self.request.user
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
         return self.request.user == self.get_object().user
        

class Delete_Resource(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Resources
    success_url = "/resources/"
    template_name = "resources/resource_confirm_delete.html"
    
    def test_func(self):
        # reads like: Is the person making the request
        # the owner of the recipe?
        recipe = self.get_object()
        return self.request.user == recipe.user
    
    
class Stories(TemplateView):
    template_name = 'resources/stories.html'