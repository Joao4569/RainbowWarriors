from django.urls import path
from .views import (Resources, Update_Resource,
                    Add_Resource, Delete_Resource,
                    Stories)

urlpatterns = [
    path('', Resources.as_view(), name='resources'),
    path('add/', Add_Resource.as_view(), name='add_resource'),
    path('update/<int:pk>/', Update_Resource.as_view(), name='update_resource'),
    path('delete/<int:pk>/', Delete_Resource.as_view(), name="delete_resource"),
    path('stories/', Stories.as_view(), name="stories"),
]
