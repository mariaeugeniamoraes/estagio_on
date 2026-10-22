
from django.db import models
from usuarios.models import Candidato
from vagas.models import Vaga


class Candidatura(models.Model):

    STATUS = [
        ('pendente', 'Pendente'),
        ('analise', 'Em análise'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]

    candidato = models.ForeignKey(
        Candidato,
        on_delete=models.CASCADE,
        related_name='candidaturas'
    )

    vaga = models.ForeignKey(
        Vaga,
        on_delete=models.CASCADE,
        related_name='candidaturas'
    )

    data_candidatura = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='pendente'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['candidato', 'vaga'],
                name='candidatura_unica_por_vaga'
            )
        ]

    def __str__(self):
        return f'{self.candidato} - {self.vaga}'

