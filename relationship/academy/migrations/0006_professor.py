# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_aluno_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='academy.Pessoa')),
                ('MatriculaProfessor', models.IntegerField(null=True, verbose_name=b'Numero de matricula do professor')),
                ('CursoProfessor', models.CharField(max_length=50, null=True, verbose_name=b'Nome do curso lecionado')),
            ],
            options={
            },
            bases=('academy.pessoa',),
        ),
    ]
