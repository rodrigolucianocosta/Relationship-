# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeCurso', models.CharField(max_length=30, null=True, verbose_name=b'nome do curso')),
                ('tipoCurso', models.CharField(max_length=1, null=True, verbose_name=b'tipo de curso', choices=[(b'A', b'EXATAS'), (b'B', b'HUMANAS')])),
                ('duracaoCurso', models.IntegerField(null=True, verbose_name=b'duracao do curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeDisciplina', models.CharField(max_length=30, null=True, verbose_name=b'nome da disciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TipoGrade', models.CharField(max_length=20, null=True, verbose_name=b'tipo de grade')),
                ('curso', models.ForeignKey(verbose_name=b'Curso', to='academy.Curso', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GradeDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Discip', models.ForeignKey(verbose_name=b'Disciplina', to='academy.Disciplina')),
                ('Estruct', models.ForeignKey(verbose_name=b'Estrutura', to='academy.Grade')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NumeroPeriodo', models.IntegerField(null=True, verbose_name=b'numero do per\xc3\xadodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NumeroSemestre', models.IntegerField(null=True, verbose_name=b'numero do semestre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeTurma', models.CharField(max_length=1, null=True, verbose_name=b'Nome da turma')),
                ('grade', models.ForeignKey(verbose_name=b'Grade', to='academy.Grade', null=True)),
                ('semestre', models.ForeignKey(verbose_name=b'Turma', to='academy.Semestre', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gradeDisciplina', models.ForeignKey(verbose_name=b'Grade Disciplina', to='academy.Grade', null=True)),
                ('turma', models.ForeignKey(verbose_name=b'Turma', to='academy.Turma', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gradedisciplina',
            name='Period',
            field=models.ForeignKey(verbose_name=b'Periodo', to='academy.Periodo'),
            preserve_default=True,
        ),
    ]
