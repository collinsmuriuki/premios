# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-24 15:10
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('premios_app', '0002_auto_20191124_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]