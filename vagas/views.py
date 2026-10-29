
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from usuarios.models import Empresa
from .forms import VagaForm
from .models import Vaga


@login_required(login_url='login')
def publicar_vaga(request):

    if request.user.tipo_usuario != 'empresa':
        messages.error(
            request,
            'Somente empresas podem publicar vagas.'
        )
        return redirect('home')

    empresa = get_object_or_404(
        Empresa,
        usuario=request.user
    )

    if request.method == 'POST':
        form = VagaForm(request.POST)

        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.empresa = empresa
            vaga.save()

            messages.success(
                request,
                'Vaga publicada com sucesso!'
            )

            return redirect('perfil_empresa')

    else:
        form = VagaForm()

    return render(
        request,
        'vagas/publicar_vaga.html',
        {'form': form}
    )

@login_required(login_url='login')
def minhas_vagas(request):

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

    vagas = Vaga.objects.filter(
        empresa=empresa
    ).order_by('-data_publicacao')

    return render(
        request,
        'vagas/minhas_vagas.html',
        {'vagas': vagas}
    )


@login_required(login_url='login')
def editar_vaga(request, vaga_id):

    if request.user.tipo_usuario != 'empresa':
        messages.error(request, 'Acesso permitido apenas para empresas.')
        return redirect('home')

    empresa = get_object_or_404(
        Empresa,
        usuario=request.user
    )

    vaga = get_object_or_404(
        Vaga,
        id=vaga_id,
        empresa=empresa
    )

    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Vaga atualizada com sucesso!'
            )

            return redirect('minhas_vagas')
    else:
        form = VagaForm(instance=vaga)

    return render(
        request,
        'vagas/editar_vaga.html',
        {'form': form, 'vaga': vaga}
    )


@login_required(login_url='login')
def excluir_vaga(request, vaga_id):

    if request.user.tipo_usuario != 'empresa':
        messages.error(request, 'Acesso permitido apenas para empresas.')
        return redirect('home')

    empresa = get_object_or_404(
        Empresa,
        usuario=request.user
    )

    vaga = get_object_or_404(
        Vaga,
        id=vaga_id,
        empresa=empresa
    )

    if request.method == 'POST':
        vaga.delete()

        messages.success(
            request,
            'Vaga excluída com sucesso!'
        )

        return redirect('minhas_vagas')

    return render(
        request,
        'vagas/excluir_vaga.html',
        {'vaga': vaga}
    )

def detalhes_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)

    return render(
        request,
        'vagas/detalhes_vaga.html',
        {'vaga': vaga}
    )

