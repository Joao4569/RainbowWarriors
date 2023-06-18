from django.urls import path
from .views import (Resources, Update_Resource,
                    Add_Resource)

urlpatterns = [
    path('', Resources.as_view(), name='resources'),
    path('add/', Add_Resource.as_view(), name='add_resource'),
    path('update/<slug:pk>', Update_Resource.as_view(), name='update_resource'),
]
