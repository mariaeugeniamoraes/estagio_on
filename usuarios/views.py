
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import CadastroCandidatoForm, CadastroEmpresaForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


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

