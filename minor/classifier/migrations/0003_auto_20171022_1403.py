# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_files_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'ordering': ['name']},
        ),
    ]
