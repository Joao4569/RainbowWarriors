from django.views.generic import (
    CreateView, ListView,
    DeleteView, UpdateView
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from .forms import ResourceForm
from .models import Resources
# johnny -testing
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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


@login_required
def update_resource(request, resource_id):
    """Edit a resource"""
    resource = get_object_or_404(Resources, pk=resource_id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated resource!')
            return redirect(reverse('resources', args=[resource.id]))
        else:
            messages.error(request,
                           'Failed to update resource. Please ensure the form is valid.')
    else:
        form = ResourceForm(instance=resource)
        messages.info(request, f'You are editing {resource.title}')

    template = 'resources/edit_resource.html'
    context = {
        'form': form,
        'resource': resource,
    }

    return render(request, template, context)
