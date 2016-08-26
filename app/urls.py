from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^new/$', views.add_match, name='add_match'),
    url(r'^search/$', views.search, name='search'),
    # Registration
    url(r'^accounts/', include('registration.backends.default.urls')),
]
