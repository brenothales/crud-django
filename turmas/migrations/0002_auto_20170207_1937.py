# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='descricaoTurma',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
    ]
