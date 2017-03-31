# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transcodertask',
            fields=[
                ('taskid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('createtime', models.DateTimeField()),
                ('size', models.CharField(max_length=50)),
                ('src', models.CharField(max_length=100)),
                ('dst', models.CharField(max_length=100)),
                ('dformate', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('bitrate', models.IntegerField()),
            ],
        ),
    ]
