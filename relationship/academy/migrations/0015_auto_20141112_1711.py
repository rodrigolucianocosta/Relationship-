# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0014_grade_anograde'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplinaaluno',
            old_name='disciplinaAluno',
            new_name='turmaDisciplina',
        ),
        migrations.AlterField(
            model_name='horario',
            name='FinalHorarioAula',
            field=models.TimeField(null=True, verbose_name=b'horario do Final da aula'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='InicioHorarioAula',
            field=models.TimeField(null=True, verbose_name=b'horario de Inicio da aula'),
        ),
    ]
