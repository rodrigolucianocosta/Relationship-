#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

TIPO_CURSO = [
	('A', 'EXATAS'),
	('B', 'HUMANAS'),
	('C', 'BIOLOGICAS')


]

class Curso(models.Model):
	#grade = models.ForeignKey(Grade,verbose_name="grade curricular",null=True)
	nomeCurso = models.CharField('nome do curso',max_length=30,null=True)
	tipoCurso = models.CharField('tipo de curso', max_length=1,choices=TIPO_CURSO,null=True)
	duracaoCurso = models.IntegerField('duracao do curso',null=True)

	def __unicode__(self):
		return self.nomeCurso


class Grade(models.Model):
	#curso = models.ForeignKey(Curso,verbose_name="Curso",null=True)
	TipoGrade = models.CharField('tipo de grade',max_length=20,null=True)


	def __unicode__(self):
		return self.TipoGrade


class Disciplina(models.Model):
	nomeDisciplina = models.CharField('nome da disciplina',max_length=30,null=True)
	cargahoraria = models.IntegerField('carga horaria',null=True)


	def __unicode__(self):
		return self.nomeDisciplina	


class Periodo(models.Model):
	NumeroPeriodo = models.IntegerField('numero do período',null =True)

	def __unicode__(self):
		return str(self.NumeroPeriodo)


class Semestre(models.Model):
	NumeroSemestre = models.IntegerField('numero do semestre',null=True)

	def __unicode__(self):
		return str(self.NumeroSemestre)	


class GradeDisciplina(models.Model):
	Estruct = models.ForeignKey(Grade,verbose_name="Estrutura",null=False)
	Period = models.ForeignKey(Periodo,verbose_name="Periodo",null=False)
	Discip = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=False)

	def __unicode__(self):
		return str(self.Period.NumeroPeriodo)


class Turma(models.Model):
	semestre = models.ForeignKey(Semestre,verbose_name="Semestre",null=True)
	grade = models.ForeignKey(Grade,verbose_name="Grade",null=True)
	periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	NomeTurma = models.CharField('Nome da turma',max_length=50,null=True)

	def __unicode__(self):
		return self.NomeTurma

	

class TurmaDisciplina(models.Model):
	gradeDisciplina = models.ForeignKey(Grade,verbose_name="Grade Disciplina",null=True)
	turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	

	def __unicode__(self):
		return self.turma.NomeTurma


'''class Pessoa(models.Model):
	NomePessoa = models.CharField('Nome',max_length=100,null=True)
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
		return self.NomePessoa
'''

'''class aluno(Pessoa):
	MatriculaAluno = models.IntegerField('Numero de matricula do aluno',max_length=50,null=True)

	def __unicode__(self):
			return self.
'''

'''
class professor(Pessoa):
	MatriculaProfessor = models.IntegerField('Numero de matricula do professor',null=True)
	CursoProfessor = models.CharField('Nome do curso lecionado',max_length=50,null=True)

	def __unicode__(self):
		return self.NomePessoa
'''
		

'''class horario(models.Model):
	InicioHorarioAula = models.DateTimeField('horario de Inicio da aula',null=True)
	FinalHorarioAula = models.DateTimeField('horario do Final da aula',null=True)

	def __unicode__(self):
		return self.InicioHorarioAula

'''

'''class TurmDiscHorario(models.Model):
	TurmaDisciplinaHorario = models.ForeignKey(horario,verbose_name="horario aula",null=True)
	#ProfessorTurmaDisciplinaHorario = models.ForeignKey(professor,verbose_name="professor",null=True)

	def __unicode__(self):
		return self.ProfessorTurmaDisciplinaHorario.NomeProfessor
'''