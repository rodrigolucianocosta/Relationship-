# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_aluno_disciplina_periodo_professor_semestre_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='estruturaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Discip', models.ForeignKey(verbose_name=b'Disciplina', to='academy.disciplina')),
                ('Estruct', models.ForeignKey(verbose_name=b'Estrutura', to='academy.estrutura')),
                ('Period', models.ForeignKey(verbose_name=b'Periodo', to='academy.periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='turma',
            name='Turma',
            field=models.ForeignKey(verbose_name=b'Turma', to='academy.semestre', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='estrutura',
            name='Estrutura',
            field=models.ForeignKey(verbose_name=b'Estrutura', to='academy.curso'),
        ),
    ]
