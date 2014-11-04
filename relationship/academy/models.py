#coding:utf-8
from django.db import models

class curso(models.Model):
	nomeCurso = models.CharField('nome do curso',max_length=30,null=True)
	duracaoCurso = models.IntegerField('duracao do curso',null=True)

	def __unicode__(self):
		return self.nomeCurso

#class semestre(models.Model):

#class aluno(models.Model):

class estrutura(models.Model):
	Estrutura = models.ForeignKey(curso,verbose_name="Evento",null=False)


	def __unicode__(self):
		return self.Nome

#class turma(models.Model):

#class periodo(models.Model):

#class disciplina(models.Model):

#class professor(models.Model):

#class horario(models.Model):
