from django.shortcuts import render, redirect
from .models import Match
from .forms import MatchForm

def index(request):
    return render(request, 'index.html', {})


def leaderboard(request):
    stats = Match.objects.all()
    return render(
        request,
        'leaderboard.html',
        {'leaderboard': stats,'page_title': 'Leaderboard'}
    )


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

    return render(request, 'add_match.html', {'form': form})
