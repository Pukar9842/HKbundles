from django.http import HttpResponse
from django.shortcuts import render
from .models import FundFarm


# /FundFarm-> index
def index(request):
    farms_info = FundFarm.objects.all()
    return HttpResponse('Fund a farm')


def availablefarms(request):
    return HttpResponse('Available Farms')
