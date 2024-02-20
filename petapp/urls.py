from django.urls import path
from .views import pets_by_breed

urlpatterns = [

    path('pets_by_breed/',pets_by_breed, name = 'pets_by_breed'),
]