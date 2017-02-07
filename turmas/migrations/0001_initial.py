# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('codigoAluno', models.IntegerField(serialize=False, primary_key=True)),
                ('nomeAluno', models.CharField(max_length=200, verbose_name=b'Nome completo')),
                ('cpf', models.CharField(unique=True, max_length=14, verbose_name=b'CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name=b'Telefone')),
                ('dataNasc', models.DateField(verbose_name=b'Data de nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('codigoTurma', models.IntegerField(serialize=False, primary_key=True)),
                ('nomeTurma', models.CharField(max_length=200, verbose_name=b'Nome da turma')),
                ('descricaoTurma', models.TextField()),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(to='turmas.Turma'),
        ),
    ]
