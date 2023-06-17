from django.shortcuts import render


# Create your views here.
# handle request to view community.html - Johnny
def community(request):
    return render(request, 'community.html')
