from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('availablefarms', views.availablefarms),
    path('services', views.services),
    path('about', views.about),
    path('contact', views.contact),
    path('buyproducts', views.buyproducts)

]
