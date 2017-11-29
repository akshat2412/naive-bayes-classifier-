# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_auto_20171022_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='image_url',
            field=models.CharField(default=b'default_url', max_length=100),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
