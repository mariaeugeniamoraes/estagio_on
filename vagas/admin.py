
from django.contrib import admin
from .models import Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'empresa',
        'bolsa_auxilio',
        'modalidade',
        'status',
        'data_publicacao',
    )

    list_filter = ('modalidade', 'status')

    search_fields = ('titulo', 'empresa__nome_empresa')

