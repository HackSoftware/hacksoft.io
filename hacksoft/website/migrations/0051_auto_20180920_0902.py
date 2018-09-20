# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_blogpostplacement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='authors',
            field=models.ManyToManyField(to='website.Teammate'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='website.Category'),
        ),
    ]
