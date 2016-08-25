from django.contrib import admin
from .models import Map, Mode, Rank, Match


class MatchAdmin(admin.ModelAdmin):
    list_display = ('pk', 'outcome', 'rounds_won', 'kills', 'deaths',
        'kill_death_ratio','score','map','mode','date',)


admin.site.register(Map)
admin.site.register(Mode)
admin.site.register(Rank)
admin.site.register(Match, MatchAdmin)
admin.site.site_header = 'CS:GO Scores'
admin.site.site_title = 'CS:GO Scores'
