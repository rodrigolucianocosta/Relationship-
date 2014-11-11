# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0010_disciplinaaluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('InicioHorarioAula', models.DateTimeField(null=True, verbose_name=b'horario de Inicio da aula')),
                ('FinalHorarioAula', models.DateTimeField(null=True, verbose_name=b'horario do Final da aula')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
