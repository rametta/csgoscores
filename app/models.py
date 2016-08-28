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

    PLACEMENTS = {
        1: '1ST',
        2: '2nd',
        3: '3rd',
        4: '4th',
        5: '5th',
    }

    rounds_won = models.PositiveSmallIntegerField(verbose_name='Rounds Won')
    rounds_lost = models.PositiveSmallIntegerField(verbose_name='Rounds Lost')
    kills = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()
    deaths = models.PositiveSmallIntegerField()
    mvps = models.PositiveSmallIntegerField(verbose_name='MVPs')
    placement = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()
    date = models.DateField()
    outcome = models.CharField(max_length=4)
    round_win_loss_ratio = models.FloatField()
    kill_death_ratio = models.FloatField()
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    def mOutcome(self):
        if self.rounds_won > self.rounds_lost:
            return "Win"
        elif self.rounds_won < self.rounds_lost:
            return "Loss"
        else:
            return "Tie"

    def mRound_win_loss_ratio(self):
        return self.rounds_won/self.rounds_lost

    def mKill_death_ratio(self):
        return self.kills/self.deaths

    def placement_str(self):
        return PLACEMENTS[self.placement]()

    def save(self, *args, **kwargs):
        # I know saving calculated fields is not the best
        # idea but I need to query based on the grouped calculations
        # and I don't want to use custom Managers
        self.outcome = self.mOutcome()
        self.round_win_loss_ratio = self.mRound_win_loss_ratio()
        self.kill_death_ratio = self.mKill_death_ratio()
        super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return self.outcome()

    class Meta:
        verbose_name_plural = 'Matches'
