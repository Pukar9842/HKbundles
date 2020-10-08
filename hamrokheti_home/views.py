from django.http import HttpResponse
from django.shortcuts import render
from .models import FundFarm


# /FundFarm-> index
def index(request):
    return render(request, 'index.html')


def availablefarms(request):
    farm_items = FundFarm.objects.all()
    return render(request, 'availablefarms.html', {'farms': farm_items})


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def buyproducts(request):
    return render(request, 'buyproducts.html')
