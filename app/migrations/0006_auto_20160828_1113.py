# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_match_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='kill_death_ratio',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='outcome',
            field=models.CharField(default='Win', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='round_win_loss_ratio',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]