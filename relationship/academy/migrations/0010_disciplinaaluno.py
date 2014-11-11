# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_auto_20141111_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disciplinaAluno', models.ForeignKey(verbose_name=b'Disciplina Aluno', to='academy.TurmaDisciplina', null=True)),
                ('turmaAluno', models.ForeignKey(verbose_name=b'Tuma Aluno', to='academy.TurmaAluno', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
