# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_auto_20141110_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='curso',
        ),
        migrations.AlterField(
            model_name='turma',
            name='NomeTurma',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Nome da turma'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='semestre',
            field=models.ForeignKey(verbose_name=b'Semestre', to='academy.Semestre', null=True),
        ),
    ]
