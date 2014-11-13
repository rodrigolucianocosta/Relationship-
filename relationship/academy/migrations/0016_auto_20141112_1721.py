# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0015_auto_20141112_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinaaluno',
            name='turmaDisciplina',
            field=models.ForeignKey(verbose_name=b'Turma Disciplina', to='academy.TurmaDisciplina', null=True),
        ),
        migrations.AlterField(
            model_name='turmaaluno',
            name='turma',
            field=models.ForeignKey(verbose_name=b'Turma', to='academy.Turma', null=True),
        ),
    ]
