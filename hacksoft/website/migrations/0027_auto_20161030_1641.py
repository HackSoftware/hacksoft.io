# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-30 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20161029_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='popup_text',
            field=wagtail.core.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='footer',
            name='links',
            field=wagtail.core.fields.StreamField((('link', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.TextBlock()), ('url', wagtail.core.blocks.URLBlock())), template='streams/footer_link.html')),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro_h1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro_h2',
            field=models.CharField(max_length=500),
        ),
    ]
