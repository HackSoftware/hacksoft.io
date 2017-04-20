# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0041_auto_20170420_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostspage',
            name='featured_article',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='website.BlogPost'),
        ),
    ]