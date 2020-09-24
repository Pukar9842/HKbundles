from django.http import HttpResponse
from django.shortcuts import render
from .models import FarmUpdate


def farm_update(request):
    farm_updates = FarmUpdate.objects.all()
    return render(request, 'followfarm.html', {'updates': farm_updates})






