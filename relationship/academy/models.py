#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

class curso(models.Model):
	nomeCurso = models.CharField('nome do curso',max_length=30,null=True)
	duracaoCurso = models.IntegerField('duracao do curso',null=True)

	def __unicode__(self):
		return self.nomeCurso

class estrutura(models.Model):
	Estrutura = models.ForeignKey(curso,verbose_name="Evento",null=False)



	def __unicode__(self):
		return self.Nome

class periodo(models.Model):
	NumeroPeriodo = models.IntegerField('numero do período',null =False)

	def __unicode__(self):
		return self.NumeroPeriodo



class disciplina(models.Model):
	NomeDisciplina = models.IntegerField('nome da disciplina',null=True)

	def __unicode__(self):
		return self.NomeDisciplina


class semestre(models.Model):
	NumeroSemestre = models.IntegerField('numero do semestre',null=True)

	def __unicode__(self):
		return self.NumeroSemestre

class aluno(models.Model):
	NomeAluno = models.CharField('Nome',max_length=100,null=True)
	CPF = models.CharField('CPF',max_length=14,unique=True,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
	UF = models.CharField('UF', max_length=2,choices=STATE_CHOICES,null=True)
	CEP = models.CharField('CEP', max_length=9,null=True)
	URL = models.URLField ('Página Pessoal', max_length=200,null=True,blank=True)

	def __unicode__(self):
		return self.Nome

class turma(models.Model):
	NomeTurma = models.CharField('Nome da turma',max_length=1,null=True)
	
	def __unicode__(self):
		return self.NomeTurma

class professor(models.Model):
	NomeProfessor = models.CharField('Nome do professor',max_length=50,null=True)

	def __unicode__(self):
		return self.NomeProfessor

		

#class horario(models.Model):
