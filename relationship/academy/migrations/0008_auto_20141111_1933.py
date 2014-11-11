# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_remove_professor_cursoprofessor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='gradedisciplina',
            name='Estruct',
            field=models.ForeignKey(verbose_name=b'Grade', to='academy.Grade'),
        ),
    ]
