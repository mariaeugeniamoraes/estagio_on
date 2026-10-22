
from django.shortcuts import render
from vagas.models import Vaga


def home(request):
    vagas_recentes = Vaga.objects.filter(
        status='aberta'
    ).select_related('empresa').order_by(
        '-data_publicacao'
    )[:6]

    contexto = {
        'vagas_recentes': vagas_recentes
    }

    return render(request, 'core/home.html', contexto)
