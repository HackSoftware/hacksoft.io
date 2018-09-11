# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-21 13:38
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160920_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howweworkpage',
            name='the_process_content',
            field=wagtail.core.fields.StreamField((('process_content', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('icon_classes', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock())), template='streams/process_content.html')),)),
        ),
    ]
