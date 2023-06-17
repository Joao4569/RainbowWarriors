from django.shortcuts import render

# Create your views here.

# handle request to view resources.html - Johnny
def resources(request):
    return render(request, 'resources.html')