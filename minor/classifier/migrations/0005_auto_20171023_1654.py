# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0004_auto_20171023_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='image_url',
            new_name='image_name',
        ),
    ]
