from django.shortcuts import render
from app.models import Map, Match

def index(request):
    all_maps = Map.objects.all()
    return render(request, 'index.html', {'maps': all_maps})

def leaderboard(request):
    stats = Match.objects.all()
    return render(
        request,
        'leaderboard.html',
        {'leaderboard': stats, 'page_title': 'Leaderboard'}
    )
