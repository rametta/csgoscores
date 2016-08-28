from django import forms
from .models import Match


class MatchForm(forms.ModelForm):
    rounds_won = forms.IntegerField(max_value=16, min_value=0)
    rounds_lost = forms.IntegerField(max_value=16, min_value=0)
    kills = forms.IntegerField(min_value=0)
    assists = forms.IntegerField(min_value=0)
    deaths = forms.IntegerField(min_value=0)
    mvps = forms.IntegerField(max_value=30, min_value=0)
    placement = forms.IntegerField(max_value=5, min_value=1)
    score = forms.IntegerField(max_value=500)
    date = forms.DateField()

    class Meta:
        model = Match
        fields = (
            'rank',
            'mode',
            'map',
        )
