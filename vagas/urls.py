from django.urls import path
from . import views

urlpatterns = [
    path(
        'publicar/',
        views.publicar_vaga,
        name='publicar_vaga'
    ),
    path(
        'minhas/',
        views.minhas_vagas,
        name='minhas_vagas'
    ),
    path('editar/<int:vaga_id>/', views.editar_vaga, name='editar_vaga'),
    path('excluir/<int:vaga_id>/', views.excluir_vaga, name='excluir_vaga'),
    path('detalhes/<int:vaga_id>/', views.detalhes_vaga, name='detalhes_vaga'),
]