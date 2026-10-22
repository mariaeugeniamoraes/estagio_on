
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import CadastroCandidatoForm, CadastroEmpresaForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Candidato, Empresa
from .forms import EditarPerfilCandidatoForm
from .forms import EditarPerfilEmpresaForm


def cadastro_candidato(request):
    if request.method == 'POST':
        form = CadastroCandidatoForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = CadastroCandidatoForm()

    return render(request, 'usuarios/cadastro_candidato.html', {
        'form': form
    })


def cadastro_empresa(request):
    if request.method == 'POST':
        form = CadastroEmpresaForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('home')
    else:
        form = CadastroEmpresaForm()

    return render(request, 'usuarios/cadastro_empresa.html', {
        'form': form
    })

def entrar(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})


def sair(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Você saiu da sua conta.')
        return redirect('home')

    return redirect('home')

@login_required(login_url='login')
def perfil_candidato(request):
    if request.user.tipo_usuario != 'candidato':
        messages.error(request, 'Esta página é exclusiva para estudantes.')
        return redirect('home')

    candidato = get_object_or_404(
        Candidato,
        usuario=request.user
    )

    return render(request, 'usuarios/perfil_candidato.html', {
        'candidato': candidato
    })

@login_required(login_url='login')
def editar_perfil_candidato(request):

    if request.user.tipo_usuario != 'candidato':
        messages.error(request, 'Esta página é exclusiva para estudantes.')
        return redirect('home')

    candidato = get_object_or_404(
        Candidato,
        usuario=request.user
    )

    if request.method == 'POST':
        form = EditarPerfilCandidatoForm(
            request.POST,
            instance=candidato
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Perfil atualizado com sucesso!'
            )

            return redirect('perfil_candidato')

    else:
        form = EditarPerfilCandidatoForm(
            instance=candidato
        )

    return render(
        request,
        'usuarios/editar_perfil_candidato.html',
        {'form': form}
    )

@login_required(login_url='login')
def perfil_empresa(request):

    if request.user.tipo_usuario != 'empresa':
        messages.error(
            request,
            'Esta página é exclusiva para empresas.'
        )
        return redirect('home')

    empresa = get_object_or_404(
        Empresa,
        usuario=request.user
    )

    return render(
        request,
        'usuarios/perfil_empresa.html',
        {'empresa': empresa}
    )

@login_required(login_url='login')
def editar_perfil_empresa(request):

    if request.user.tipo_usuario != 'empresa':
        messages.error(request, 'Esta página é exclusiva para empresas.')
        return redirect('home')

    empresa = get_object_or_404(
        Empresa,
        usuario=request.user
    )

    if request.method == 'POST':
        form = EditarPerfilEmpresaForm(
            request.POST,
            instance=empresa
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Perfil da empresa atualizado com sucesso!'
            )

            return redirect('perfil_empresa')

    else:
        form = EditarPerfilEmpresaForm(instance=empresa)

    return render(
        request,
        'usuarios/editar_perfil_empresa.html',
        {'form': form}
    )

