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
'''
from models import semestre
#from models import aluno
from models import turma
#from models import professor
from models import horario
'''
# Register your models here.

class cursoAdmin(admin.ModelAdmin):
	list_display = ['nomeCurso']
	#list_filter = ['']
	#search_fields = ['']
	save_as = True
	
class gradeAdmin(admin.ModelAdmin):
	list_display = ['TipoGrade']
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
'''
class semestreAdmin(admin.ModelAdmin):
	list_display = ['NumeroSemestre']
'''
'''class alunoAdmin(admin.ModelAdmin):
	list_display = ['NomeAluno','CPF']
	save_as = True
'''
'''
class turmaAdmin(admin.ModelAdmin):
	list_display = ['NomeTurma']
	save_as = True
'''
'''class professorAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa']
	save_as = True
'''
'''
class estruturaAdmin(admin.ModelAdmin):
	list_display = ['TipoEstrutura']
	save_as = True			

class estruturaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Period','Estruct','Discip']	
	save_as = True	



class horarioAdmin(admin.ModelAdmin):
	list_display = ['InicioHorarioAula','FinalHorarioAula']	
	save_as= True		
'''
admin.site.register(Curso,cursoAdmin)
admin.site.register(Grade,gradeAdmin)
admin.site.register(Disciplina,disciplinaAdmin)
admin.site.register(Periodo,periodoAdmin)
admin.site.register(Semestre,semestreAdmin)
admin.site.register(GradeDisciplina,gradeDisciplinaAdmin)
admin.site.register(Turma,turmaAdmin)
admin.site.register(TurmaDisciplina,turmaDisciplinaAdmin)
'''
admin.site.register(semestre,semestreAdmin)
#admin.site.register(aluno,alunoAdmin)
#admin.site.register(professor,professorAdmin)
admin.site.register(Grade,gradeAdmin)
admin.site.register(horario,horarioAdmin)

'''