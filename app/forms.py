from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = (
            'rounds_won',
            'rounds_lost',
            'kills',
            'assists',
            'deaths',
            'mvps',
            'placement',
            'score',
            'date',
            'rank',
            'mode',
            'map',
        )
