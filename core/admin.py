from django.contrib import admin
from .models import Cargos, Servicos, Funcionario, Recursos


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'activo', 'modificado')


@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'utilidade', 'icone', 'activo')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'activo', 'modificado')


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servico', 'activo', 'modificado')
