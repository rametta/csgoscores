from django.db import models
from django.contrib.auth.models import User


class Map(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Mode(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Rank(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Match(models.Model):
    rounds_won = models.PositiveSmallIntegerField(verbose_name='Rounds Won')
    rounds_lost = models.PositiveSmallIntegerField(verbose_name='Rounds Lost')
    kills = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()
    deaths = models.PositiveSmallIntegerField()
    mvps = models.PositiveSmallIntegerField(verbose_name='MVPs')
    placement = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()
    date = models.DateField()
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    def outcome(self):
        if self.rounds_won > self.rounds_lost:
            return "Win"
        elif self.rounds_won < self.rounds_lost:
            return "lost"
        else:
            return "Tie"

    def round_win_loss_ratio(self):
        return "{0:.2f}".format(self.rounds_won/self.rounds_lost)

    def kill_death_ratio(self):
        return "{0:.2f}".format(self.kills/self.deaths)

    def __str__(self):
        return self.outcome()

    class Meta:
        verbose_name_plural = 'Matches'
