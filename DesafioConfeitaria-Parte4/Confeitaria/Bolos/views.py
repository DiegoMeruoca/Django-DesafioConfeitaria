from django.shortcuts import render
from .models import Bolo

def home(request):
    return render(request,"Bolos/home.html")

def listagembolo(request):
    data = {}
    data["bolos"]= Bolo.objects.all()
    return render(request,"Bolos/listagembolo.html", data)
