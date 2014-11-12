# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0012_turmdischorario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='TipoGrade',
        ),
        migrations.AddField(
            model_name='grade',
            name='nomeGrade',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Nome de grade'),
            preserve_default=True,
        ),
    ]
