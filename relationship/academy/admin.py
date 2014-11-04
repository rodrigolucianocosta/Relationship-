#coding:utf-8
from django.contrib import admin
from models import curso
from models import estrutura
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

admin.site.register(curso,cursoAdmin)
