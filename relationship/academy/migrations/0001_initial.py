# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeCurso', models.CharField(max_length=30, null=True, verbose_name=b'nome do curso')),
                ('duracaoCurso', models.IntegerField(null=True, verbose_name=b'duracao do curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='estrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Estrutura', models.ForeignKey(verbose_name=b'Evento', to='academy.curso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
