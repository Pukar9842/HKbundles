from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('availablefarms', views.availablefarms)
]
