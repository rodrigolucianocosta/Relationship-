# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_auto_20141106_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrutura',
            name='TipoEstrutura',
            field=models.CharField(max_length=20, null=True, verbose_name=b'tipo de estrutura'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='NomeDisciplina',
            field=models.CharField(max_length=30, null=True, verbose_name=b'nome da disciplina'),
        ),
        migrations.AlterField(
            model_name='estrutura',
            name='Estrutura',
            field=models.ForeignKey(verbose_name=b'Estrutura', to='academy.curso', null=True),
        ),
    ]
