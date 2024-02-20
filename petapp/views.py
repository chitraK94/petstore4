from django.shortcuts import render
from .models import Pet

def pets_by_breed(request):

    lab = Pet.objects.get_pet_by_breed('lab')
    return render(request, 'petapp/pets_by_breed.html', {'lab':lab})
