from django.http import HttpResponse
from django.shortcuts import render


# /FundFarm-> index
def index(request):
    return HttpResponse('Fund our farm')


def availablefarms(request):
    return HttpResponse('Available Farms')
