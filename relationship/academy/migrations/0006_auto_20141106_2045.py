# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_auto_20141106_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turma',
            old_name='Turma',
            new_name='Semestre',
        ),
    ]
