from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
     # Path to Community app URL's -  Johnny
    path('community/', include('community.urls')),
]
