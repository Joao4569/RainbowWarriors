from django.shortcuts import render

# Create your views here.


# handle request to view resources.html - Johnny
def resources(request):
    template = 'resources/resources.html'
    return render(request, template)
