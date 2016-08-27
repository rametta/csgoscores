from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Match
from .forms import MatchForm

def index(request):
    return render(request, 'index.html', {})


def leaderboard(request):
    #get all users groupby sum stats
    stats = Match.objects.all()
    return render(
        request,
        'leaderboard.html',
        {'leaderboard': stats,'page_title': 'Leaderboard'}
    )


def search(request):
    return render(request, 'search.html', {'page_title': 'Search'})


# Players
def view_player(request, username):
    player = User.objects.get(username=username)
    matches = Match.objects.filter(player=player)
    username = player.username.title()
    return render(request, 'view_player.html', {'page_title': username, 'player': player, 'matches': matches})


def players_compare(request):
    return render(request, 'players_compare.html', {'page_title': 'Player'})


# Matches
@login_required
def add_match(request):
    if request.method == 'POST':
        form = MatchForm(data=request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.player = request.user
            match.save()
            return redirect('leaderboard')
    else:
        form = MatchForm()

    return render(request, 'add_match.html', {'form': form, 'page_title': 'Add Score'})


@login_required
def edit_match(request, id):
    return render(request, 'edit_match.html', {'page_title': 'Match'})


def view_match(request, match):
    match = Match.objects.get(id=match)
    return render(request, 'view_match.html', {'page_title': match.date, 'match': match})
