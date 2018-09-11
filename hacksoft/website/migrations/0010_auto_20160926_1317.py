# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('website', '0009_portfoliopage'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='header_text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='intro',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
