from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('cadastro/empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('entrar/', views.entrar, name='login'),
    path('sair/', views.sair, name='logout'),
]