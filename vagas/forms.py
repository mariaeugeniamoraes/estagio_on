
from django import forms
from .models import Vaga


class VagaForm(forms.ModelForm):

    class Meta:
        model = Vaga

        fields = [
            'titulo',
            'descricao',
            'requisitos',
            'bolsa_auxilio',
            'modalidade',
            'cidade',
            'carga_horaria',
            'status'
        ]

        labels = {
            'titulo': 'Título da vaga',
            'descricao': 'Descrição da vaga',
            'requisitos': 'Requisitos',
            'bolsa_auxilio': 'Bolsa-auxílio (R$)',
            'modalidade': 'Modalidade',
            'cidade': 'Cidade',
            'carga_horaria': 'Carga horária semanal',
            'status': 'Status da vaga',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
            'requisitos': forms.Textarea(attrs={'rows': 4}),
            'bolsa_auxilio': forms.NumberInput(
                attrs={'min': '0', 'step': '0.01'}
            ),
            'carga_horaria': forms.NumberInput(
                attrs={'min': '1'}
            ),
        }
