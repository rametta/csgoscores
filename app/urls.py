from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^search/$', views.search, name='search'),

    # Matches
    url(r'^new/$', views.add_match, name='add_match'),
    url(r'^match/(?P<match>[0-9]+)/$', views.view_match, name='view_match'),
    url(r'^match/(?P<match>[0-9]+)/edit/$', views.edit_match, name='edit_match'),

    # Players
    url(r'^player/(?P<username>[A-Za-z-_]+)/$', views.view_player, name='view_player'),
    url(r'^player1/(?P<player1>[A-Za-z-_]+)/player2/(?P<player2>[A-Za-z-_]+)/$', views.players_compare, name='players_compare'),

    # Registration
    url(r'^accounts/', include('registration.backends.default.urls')),
]
