from django.urls import path
from .views import (Resources, Add_Resource)
from . import views

urlpatterns = [
    path('', Resources.as_view(), name='resources'),
    path('add/', Add_Resource.as_view(), name='add_resource'),
    path('update/<int:resource_id>/', views.update_resource, name='update_resource'),
]
