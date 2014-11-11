# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20141110_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='periodo',
            field=models.ForeignKey(verbose_name=b'Periodo', to='academy.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='curso',
            name='tipoCurso',
            field=models.CharField(max_length=1, null=True, verbose_name=b'tipo de curso', choices=[(b'A', b'EXATAS'), (b'B', b'HUMANAS'), (b'C', b'BIOLOGICAS')]),
        ),
    ]
