from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Animal

# Create your views here.
def animals(request):
    all_animals_list=Animal.objects.all()
    print(all_animals_list)
    output=', '.join([a.animalName for a in all_animals_list])
    print(output)
    return render(request, 'petshop/index.html')

def teste(request):
    all_animals_list=Animal.objects.all()
    context=list()
    for animal in all_animals_list:
        context.append(animal.animalName)
        context.append(animal.animalSpecie)
    return render(request, 'petshop/teste.html', {'context': context})