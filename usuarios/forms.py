
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Usuario, Candidato, Empresa


# ==========================================
# CADASTRO DO ESTUDANTE
# ==========================================

class CadastroCandidatoForm(UserCreationForm):

    nome_completo = forms.CharField(
        max_length=150,
        label='Nome completo'
    )

    email = forms.EmailField(
        label='E-mail'
    )

    curso = forms.CharField(
        max_length=100,
        label='Curso'
    )

    faculdade = forms.CharField(
        max_length=150,
        label='Faculdade'
    )

    periodo = forms.IntegerField(
        min_value=1,
        label='Período'
    )

    telefone = forms.CharField(
        max_length=20,
        required=False,
        label='Telefone'
    )

    cidade = forms.CharField(
        max_length=100,
        label='Cidade'
    )

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'nome_completo',
            'curso',
            'faculdade',
            'periodo',
            'telefone',
            'cidade',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    @transaction.atomic
    def save(self, commit=True):

        if not commit:
            raise ValueError(
                'O cadastro deve ser salvo com commit=True.'
            )

        usuario = super().save(commit=False)

        usuario.email = self.cleaned_data['email']
        usuario.tipo_usuario = 'candidato'
        usuario.save()

        Candidato.objects.create(
            usuario=usuario,
            nome_completo=self.cleaned_data['nome_completo'],
            curso=self.cleaned_data['curso'],
            faculdade=self.cleaned_data['faculdade'],
            periodo=self.cleaned_data['periodo'],
            telefone=self.cleaned_data['telefone'],
            cidade=self.cleaned_data['cidade'],
        )

        return usuario


# ==========================================
# CADASTRO DA EMPRESA
# ==========================================

class CadastroEmpresaForm(UserCreationForm):

    nome_empresa = forms.CharField(
        max_length=150,
        label='Nome da empresa'
    )

    email = forms.EmailField(
        label='E-mail corporativo'
    )

    cnpj = forms.CharField(
        min_length=14,
        max_length=14,
        label='CNPJ'
    )

    descricao = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label='Descrição da empresa'
    )

    cidade = forms.CharField(
        max_length=100,
        label='Cidade'
    )

    site = forms.URLField(
        required=False,
        label='Site'
    )

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'nome_empresa',
            'cnpj',
            'descricao',
            'cidade',
            'site',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']

        if not cnpj.isascii() or not cnpj.isdigit():
            raise forms.ValidationError(
                'O CNPJ deve conter 14 números.'
            )

        if Empresa.objects.filter(cnpj=cnpj).exists():
            raise forms.ValidationError(
                'Este CNPJ já está cadastrado.'
            )

        return cnpj

    @transaction.atomic
    def save(self, commit=True):

        if not commit:
            raise ValueError(
                'O cadastro deve ser salvo com commit=True.'
            )

        usuario = super().save(commit=False)

        usuario.email = self.cleaned_data['email']
        usuario.tipo_usuario = 'empresa'
        usuario.save()

        Empresa.objects.create(
            usuario=usuario,
            nome_empresa=self.cleaned_data['nome_empresa'],
            cnpj=self.cleaned_data['cnpj'],
            descricao=self.cleaned_data['descricao'],
            cidade=self.cleaned_data['cidade'],
            site=self.cleaned_data['site'],
        )

        return usuario


# ==========================================
# EDITAR PERFIL DO ESTUDANTE
# ==========================================

class EditarPerfilCandidatoForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-mail',
        required=True
    )

    class Meta:
        model = Candidato

        fields = [
            'nome_completo',
            'curso',
            'faculdade',
            'periodo',
            'telefone',
            'cidade'
        ]

        labels = {
            'nome_completo': 'Nome completo',
            'curso': 'Curso',
            'faculdade': 'Faculdade',
            'periodo': 'Período',
            'telefone': 'Telefone',
            'cidade': 'Cidade',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['email'].initial = self.instance.usuario.email

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if Usuario.objects.filter(
            email__iexact=email
        ).exclude(pk=self.instance.usuario_id).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    @transaction.atomic
    def save(self, commit=True):

        candidato = super().save(commit=False)

        candidato.usuario.email = self.cleaned_data['email']

        if commit:
            candidato.usuario.save()
            candidato.save()
            self.save_m2m()

        return candidato


# ==========================================
# EDITAR PERFIL DA EMPRESA
# ==========================================

class EditarPerfilEmpresaForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-mail corporativo',
        required=True
    )

    class Meta:
        model = Empresa

        fields = [
            'nome_empresa',
            'descricao',
            'cidade',
            'site'
        ]

        labels = {
            'nome_empresa': 'Nome da empresa',
            'descricao': 'Descrição da empresa',
            'cidade': 'Cidade',
            'site': 'Site oficial',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['email'].initial = self.instance.usuario.email

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if Usuario.objects.filter(
            email__iexact=email
        ).exclude(pk=self.instance.usuario_id).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    @transaction.atomic
    def save(self, commit=True):

        empresa = super().save(commit=False)

        empresa.usuario.email = self.cleaned_data['email']

        if commit:
            empresa.usuario.save()
            empresa.save()
            self.save_m2m()

        return empresa
