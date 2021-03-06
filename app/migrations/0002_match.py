# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_won', models.PositiveSmallIntegerField()),
                ('rounds_lost', models.PositiveSmallIntegerField()),
                ('kills', models.PositiveSmallIntegerField()),
                ('assists', models.PositiveSmallIntegerField()),
                ('deaths', models.PositiveSmallIntegerField()),
                ('mvps', models.PositiveSmallIntegerField()),
                ('placement', models.PositiveSmallIntegerField()),
                ('score', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Map')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Mode')),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Rank')),
            ],
        ),
    ]
