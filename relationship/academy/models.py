#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

class curso(models.Model):
	nomeCurso = models.CharField('nome do curso',max_length=30,null=True)
	duracaoCurso = models.IntegerField('duracao do curso',null=True)

	def __unicode__(self):
		return self.nomeCurso


class estrutura(models.Model):
	Estrutura = models.ForeignKey(curso,verbose_name="Estrutura",null=True)
	TipoEstrutura = models.CharField('tipo de estrutura',max_length=20,null=True)


	def __unicode__(self):
		return self.TipoEstrutura


class disciplina(models.Model):
	NomeDisciplina = models.CharField('nome da disciplina',max_length=30,null=True)

	def __unicode__(self):
		return self.NomeDisciplina	


class periodo(models.Model):
	NumeroPeriodo = models.IntegerField('numero do período',null =True)

	def __unicode__(self):
		return str(self.NumeroPeriodo)

class estruturaDisciplina(models.Model):
	Estruct = models.ForeignKey(estrutura,verbose_name="Estrutura",null=False)
	Period = models.ForeignKey(periodo,verbose_name="Periodo",null=False)
	Discip = models.ForeignKey(disciplina,verbose_name="Disciplina",null=False)

	def __unicode__(self):
		return self.Period.NumeroPeriodo



class semestre(models.Model):
	NumeroSemestre = models.IntegerField('numero do semestre',null=True)

	def __unicode__(self):
		return self.NumeroSemestre


class turma(models.Model):
	Turma = models.ForeignKey(semestre,verbose_name="Turma",null=True)	
	NomeTurma = models.CharField('Nome da turma',max_length=1,null=True)

	def __unicode__(self):
		return self.NomeTurma	

class TurmaDisciplina(models.Model):
	Turma = models.ForeignKey(turma,verbose_name="Turma",null=True)
	estruturaDisciplina = models.ForeignKey(estruturaDisciplina,verbose_name="Estrutura Disciplina",null=True)

	def __unicode__(self):
		return self.Turma.NomeTurma


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


class professor(models.Model):
	NomeProfessor = models.CharField('Nome do professor',max_length=50,null=True)

	def __unicode__(self):
		return self.NomeProfessor

		

'''class horario(models.Model):
	HorarioAula = models.DateTimeField()
'''