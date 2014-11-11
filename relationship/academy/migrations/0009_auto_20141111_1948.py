# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0008_auto_20141111_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aluno', models.ForeignKey(verbose_name=b'Aluno', to='academy.Aluno', null=True)),
                ('turma', models.ForeignKey(verbose_name=b'Turma', to='academy.TurmaDisciplina', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grade',
            name='curso',
            field=models.ForeignKey(verbose_name=b'Curso', to='academy.Curso', null=True),
            preserve_default=True,
        ),
    ]
