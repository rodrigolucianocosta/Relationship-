#coding:utf-8
from django.contrib import admin
from models import curso
from models import estrutura
from models import periodo
from models import disciplina
from models import semestre
#from models import aluno
from models import turma
from models import professor
from models import estruturaDisciplina
from models import TurmaDisciplina
from models import horario

# Register your models here.

class cursoAdmin(admin.ModelAdmin):
	list_display = ['nomeCurso']
	#list_filter = ['']
	#search_fields = ['']
	save_as = True
	
'''class estruturaAdmin(admin.ModelAdmin):
list_display = ['']
#list_filter = ['']
#search_fields = ['']
save_as = True
'''

class periodoAdmin(admin.ModelAdmin):
	list_display = ['NumeroPeriodo']
	save_as = True

class disciplinaAdmin(admin.ModelAdmin):
	list_display = ['NomeDisciplina']
	save_as = True

class semestreAdmin(admin.ModelAdmin):
	list_display = ['NumeroSemestre']

'''class alunoAdmin(admin.ModelAdmin):
	list_display = ['NomeAluno','CPF']
	save_as = True
'''
class turmaAdmin(admin.ModelAdmin):
	list_display = ['NomeTurma']
	save_as = True

class professorAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa']
	save_as = True

class estruturaAdmin(admin.ModelAdmin):
	list_display = ['TipoEstrutura']
	save_as = True			

class estruturaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Period','Estruct','Discip']	
	save_as = True	

class TurmaDisciplinaAdmin(admin.ModelAdmin):
	list_display = ['Turma','estruturaDisciplina']

class horarioAdmin(admin.ModelAdmin):
	list_display = ['InicioHorarioAula','FinalHorarioAula']	
	save_as= True		

admin.site.register(curso,cursoAdmin)
admin.site.register(periodo,periodoAdmin)
admin.site.register(disciplina,disciplinaAdmin)
admin.site.register(semestre,semestreAdmin)
#admin.site.register(aluno,alunoAdmin)
admin.site.register(turma,turmaAdmin)
admin.site.register(professor,professorAdmin)
admin.site.register(estrutura,estruturaAdmin)
admin.site.register(estruturaDisciplina,estruturaDisciplinaAdmin)
admin.site.register(TurmaDisciplina,TurmaDisciplinaAdmin)
admin.site.register(horario,horarioAdmin)

