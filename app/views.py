from django.shortcuts import render
from app.models import Map

def index(request):
    all_maps = Map.objects.all()
    return render(request, 'index.html', {'maps': all_maps})
