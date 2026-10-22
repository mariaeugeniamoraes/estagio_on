from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    TIPOS_USUARIO = [
        ('candidato', 'Candidato'),
        ('empresa', 'Empresa'),
    ]

    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPOS_USUARIO,
        default='candidato'
    )

    def __str__(self):
        return self.username

class Candidato(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='perfil_candidato'
    )

    nome_completo = models.CharField(max_length=150)
    curso = models.CharField(max_length=100)
    faculdade = models.CharField(max_length=150)
    periodo = models.PositiveIntegerField()
    telefone = models.CharField(max_length=20, blank=True)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo


class Empresa(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='perfil_empresa'
    )

    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, unique=True)
    descricao = models.TextField(blank=True)
    cidade = models.CharField(max_length=100)
    site = models.URLField(blank=True)

    def __str__(self):
        return self.nome_empresa