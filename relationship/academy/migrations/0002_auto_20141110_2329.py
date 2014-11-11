# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplina',
            old_name='NomeDisciplina',
            new_name='nomeDisciplina',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='cargahoraria',
            field=models.IntegerField(null=True, verbose_name=b'carga horaria'),
            preserve_default=True,
        ),
    ]
