
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Candidato, Empresa


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Tipo de usuário', {'fields': ('tipo_usuario',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tipo de usuário', {'fields': ('tipo_usuario',)}),
    )

    list_display = (
        'username', 'email', 'tipo_usuario', 'is_staff'
    )

    list_filter = ('tipo_usuario', 'is_staff')


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_completo', 'curso', 'faculdade', 'periodo'
    )

    search_fields = ('nome_completo', 'curso', 'faculdade')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'cnpj', 'cidade')

    search_fields = ('nome_empresa', 'cnpj')

