from django.db import models

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
