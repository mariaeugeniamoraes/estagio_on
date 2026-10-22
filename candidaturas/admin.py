
from django.contrib import admin
from .models import Candidatura


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = (
        'candidato',
        'vaga',
        'status',
        'data_candidatura',
    )

    list_filter = ('status',)

    search_fields = (
        'candidato__nome_completo',
        'vaga__titulo',
    )

