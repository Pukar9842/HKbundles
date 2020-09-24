from django.http import HttpResponse
from django.shortcuts import render
from .models import FundFarm


# /FundFarm-> index
def index(request):
    farm_items = FundFarm.objects.all()
    return render(request, 'index.html', {'farms': farm_items})


def availablefarms(request):
    return HttpResponse('Available Farms')

