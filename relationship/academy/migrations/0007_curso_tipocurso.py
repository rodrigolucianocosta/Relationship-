# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_auto_20141106_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipoCurso',
            field=models.CharField(max_length=1, null=True, verbose_name=b'tipo de curso', choices=[(b'A', b'EXATAS'), (b'B', b'HUMANAS')]),
            preserve_default=True,
        ),
    ]
