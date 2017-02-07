# -*- coding: utf-8 -*-
from django.db import models

class Aluno(models.Model):
    """
    Cadastro de Alunos
    """
    codigoAluno = models.IntegerField(primary_key=True) 
    nomeAluno   = models.CharField('Nome completo', max_length=200)
    cpf         = models.CharField('CPF', max_length=14, unique=True)
    telefone    = models.CharField('Telefone', max_length=(11))
    dataNasc    = models.DateField('Data de nascimento')

    turma = models.ForeignKey('Turma')

    def __unicode__(self):
        return self.nomeAluno

class Turma(models.Model):
    
    codigoTurma = models.IntegerField(primary_key=True) 
    nomeTurma   = models.CharField('Nome da turma', max_length=200)
    descricaoTurma = models.TextField('Descrição', )


    class Meta:
        verbose_name = u'Turma'
        verbose_name_plural = u'Turmas'

    def __unicode__(self):
        return self.nomeTurma


