#coding:utf-8
from django.contrib import admin
from models import Curso
from models import Grade
from models import Disciplina
from models import Periodo
from models import Semestre
from models import GradeDisciplina
from models import Turma
from models import TurmaDisciplina
from models import Aluno
from models import Professor
from models import TurmaAluno
from models import DisciplinaAluno
from models import Horario
from models import TurmDiscHorario
'''
from models import semestre
#from models import aluno
from models import turma
from models import horario
'''
# Register your models here.

#criando inline para curso onde o aluno escolhe qual curso quer fazer
class ChoiceInline(admin.StackedInline):
	model = Grade
	extra = 3


class cursoAdmin(admin.ModelAdmin):
	list_display = ['nomeCurso']
	inlines = [ChoiceInline]
	#list_filter = ['']
	#search_fields = ['']
	save_as = True
	
class gradeAdmin(admin.ModelAdmin):
	list_display = ['TipoGrade','curso']
#list_filter = ['']
#search_fields = ['']
	save_as = True

class disciplinaAdmin(admin.ModelAdmin):
	list_display = ['nomeDisciplina','cargahoraria']
	save_as = True

class periodoAdmin(admin.ModelAdmin):
	list_display = ['NumeroPeriodo']
	save_as = True

class semestreAdmin(admin.ModelAdmin):
	list_display = ['NumeroSemestre']
	save_as = True

class gradeDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Period','Estruct','Discip']	
	save_as = True	

class turmaAdmin(admin.ModelAdmin):
	list_display = ['NomeTurma']
	save_as = True

class turmaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['turma','gradeDisciplina']
	save_as=True

class alunoAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa']
	save_as = True

class professorAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa']
	save_as = True

class turmaALunoAdmin(admin.ModelAdmin):
	list_display = ['aluno']
	save_as = True	

class disciplinaAluno(admin.ModelAdmin):
	list_display = ['turmaAluno']
	save_as= True

class horarioAdmin(admin.ModelAdmin):
	list_display = ['InicioHorarioAula','FinalHorarioAula']	
	save_as= True

class turmDiscHorario(admin.ModelAdmin):
	list_display = ['turmaDisciplina','professor','horario']
	save_as = True
'''
class semestreAdmin(admin.ModelAdmin):
	list_display = ['NumeroSemestre']

class turmaAdmin(admin.ModelAdmin):
	list_display = ['NomeTurma']
	save_as = True


class estruturaAdmin(admin.ModelAdmin):
	list_display = ['TipoEstrutura']
	save_as = True			

class estruturaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Period','Estruct','Discip']	
	save_as = True	
		
'''
admin.site.register(Curso,cursoAdmin)
admin.site.register(Grade,gradeAdmin)
admin.site.register(Disciplina,disciplinaAdmin)
admin.site.register(Periodo,periodoAdmin)
admin.site.register(Semestre,semestreAdmin)
admin.site.register(GradeDisciplina,gradeDisciplinaAdmin)
admin.site.register(Turma,turmaAdmin)
admin.site.register(TurmaDisciplina,turmaDisciplinaAdmin)
admin.site.register(Aluno,alunoAdmin)
admin.site.register(Professor,professorAdmin)
admin.site.register(TurmaAluno,turmaALunoAdmin)
admin.site.register(DisciplinaAluno,disciplinaAluno)
admin.site.register(Horario,horarioAdmin)
admin.site.register(TurmDiscHorario,turmDiscHorario)

'''
admin.site.register(semestre,semestreAdmin)
#admin.site.register(aluno,alunoAdmin)
admin.site.register(Grade,gradeAdmin)
'''