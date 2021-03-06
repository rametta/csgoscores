from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum, Avg
from .models import Match
from .forms import MatchForm

def index(request):
    return render(request, 'index.html', {})


def leaderboard(request):
    stats = Match.objects.values('player__username').annotate(
        pSumKills = Sum('kills'),
        pSumDeaths = Sum('deaths'),
        pSumMVPs = Sum('mvps'),
        pSumAssists = Sum('assists'),
        pSumRoundsWon = Sum('rounds_won'),
        pSumRoundsLost = Sum('rounds_lost'),
        pAvgKD = Avg('kill_death_ratio')
    ).order_by('-pSumKills')

    return render(
        request,
        'leaderboard.html',
        {'leaderboard': stats,'page_title': 'Leaderboard'}
    )


def search(request):
    return render(request, 'search.html', {'page_title': 'Search'})


# Players
def view_player(request, username):
    matches = Match.objects.filter(player__username=username)

    counts = {
        "kills": matches.aggregate(Sum('kills')),
        "deaths": matches.aggregate(Sum('deaths')),
        "assists": matches.aggregate(Sum('assists')),
        "rounds_won": matches.aggregate(Sum('rounds_won')),
        "rounds_lost": matches.aggregate(Sum('rounds_lost')),
        "mvps": matches.aggregate(Sum('mvps')),
        "avg_kd": matches.aggregate(Avg('kill_death_ratio')),
        "avg_round_wl": matches.aggregate(Avg('round_win_loss_ratio')),
        "matches_won": matches.filter(outcome='Win').count(),
        "matches_lost": matches.filter(outcome='Loss').count(),
        "matches_tied": matches.filter(outcome='Tie').count(),
    }

    if counts["matches_won"]==0:
        matches_wl = 0
    elif counts["matches_lost"]==0:
        matches_wl = counts["matches_won"]
    else:
        matches_wl = counts["matches_won"]/counts["matches_lost"]

    data = serializers.serialize("json", matches)
    return render(request, 'view_player.html', {'page_title': username, 'matches': matches, 'data': data})


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
    matchJSON = serializers.serialize('json',  [match,])
    return render(request, 'view_match.html', {'page_title': match.outcome, 'match': match, 'matchJSON': matchJSON})
