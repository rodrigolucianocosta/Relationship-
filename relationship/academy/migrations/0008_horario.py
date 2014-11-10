# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_curso_tipocurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('InicioHorarioAula', models.DateTimeField()),
                ('FinalHorarioAula', models.DateTimeField()),
                ('TurmaDisciplinaHorario', models.ForeignKey(verbose_name=b'Turma Disciplina horario', to='academy.TurmaDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
