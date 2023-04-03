from django.contrib import admin

# Register your models here.

from .models import Cargo, Servico, Funcionario, Recurso


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificacao')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo',  'modificacao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modificacao')
