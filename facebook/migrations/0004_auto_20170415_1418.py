# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_auto_20170415_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookid',
            name='fb_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='facebookid',
            name='pi_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
