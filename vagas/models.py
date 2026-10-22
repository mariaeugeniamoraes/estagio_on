
from django.db import models
from usuarios.models import Empresa


class Vaga(models.Model):

    MODALIDADES = [
        ('presencial', 'Presencial'),
        ('remoto', 'Remoto'),
        ('hibrido', 'Híbrido'),
    ]

    STATUS = [
        ('aberta', 'Aberta'),
        ('encerrada', 'Encerrada'),
    ]

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='vagas'
    )

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    requisitos = models.TextField()

    bolsa_auxilio = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    modalidade = models.CharField(
        max_length=20,
        choices=MODALIDADES
    )

    cidade = models.CharField(max_length=100)

    carga_horaria = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='aberta'
    )

    data_publicacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo
