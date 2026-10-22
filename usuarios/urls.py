
from django.urls import path
from . import views

urlpatterns = [
    # Cadastro
    path(
        'cadastro/candidato/',
        views.cadastro_candidato,
        name='cadastro_candidato'
    ),

    path(
        'cadastro/empresa/',
        views.cadastro_empresa,
        name='cadastro_empresa'
    ),

    # Login e logout
    path(
        'entrar/',
        views.entrar,
        name='login'
    ),

    path(
        'sair/',
        views.sair,
        name='logout'
    ),

    # Perfil do estudante
    path(
        'perfil/candidato/',
        views.perfil_candidato,
        name='perfil_candidato'
    ),

    path(
        'perfil/candidato/editar/',
        views.editar_perfil_candidato,
        name='editar_perfil_candidato'
    ),

    # Perfil da empresa
    path(
        'perfil/empresa/',
        views.perfil_empresa,
        name='perfil_empresa'
    ),

    path(
        'perfil/empresa/editar/',
        views.editar_perfil_empresa,
        name='editar_perfil_empresa'
    ),
]
