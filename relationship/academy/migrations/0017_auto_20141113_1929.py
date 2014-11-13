# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0016_auto_20141112_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmadisciplina',
            name='gradeDisciplina',
            field=models.ForeignKey(verbose_name=b'Grade Disciplina', to='academy.GradeDisciplina', null=True),
        ),
    ]
