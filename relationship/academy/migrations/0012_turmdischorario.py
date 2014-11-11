# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0011_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmDiscHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.ForeignKey(verbose_name=b'Horario', to='academy.Horario', null=True)),
                ('professor', models.ForeignKey(verbose_name=b'Professor', to='academy.Professor', null=True)),
                ('turmaDisciplina', models.ForeignKey(verbose_name=b' Turma DisciplinaAluno', to='academy.TurmaDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
