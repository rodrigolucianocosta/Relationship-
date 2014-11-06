# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_auto_20141106_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaDisciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Turma', models.ForeignKey(verbose_name=b'Turma', to='academy.turma', null=True)),
                ('estruturaDisciplina', models.ForeignKey(verbose_name=b'Estrutura Disciplina', to='academy.estruturaDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='NumeroPeriodo',
            field=models.IntegerField(null=True, verbose_name=b'numero do per\xc3\xadodo'),
        ),
    ]
