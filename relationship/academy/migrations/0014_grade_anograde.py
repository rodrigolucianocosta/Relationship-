# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0013_auto_20141111_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='AnoGrade',
            field=models.DateField(null=True, verbose_name=b'Ano da Grade'),
            preserve_default=True,
        ),
    ]
