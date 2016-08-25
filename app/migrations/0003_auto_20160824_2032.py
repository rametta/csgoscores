# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='mvps',
            field=models.PositiveSmallIntegerField(verbose_name='MVPs'),
        ),
        migrations.AlterField(
            model_name='match',
            name='rounds_lost',
            field=models.PositiveSmallIntegerField(verbose_name='Rounds Lost'),
        ),
        migrations.AlterField(
            model_name='match',
            name='rounds_won',
            field=models.PositiveSmallIntegerField(verbose_name='Rounds Won'),
        ),
    ]