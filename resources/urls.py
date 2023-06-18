from django.urls import path
from .views import Resources

urlpatterns = [
    path('', Resources.as_view(), name='resources'),
]
