from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import clienteForm


# NOVO CLIENTE
@login_required
def novoCliente(request):
    form = clienteForm(request.POST or None, request.FILES or None)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')  # COLOCAR PRA REDIRECIONAR PRA UMA PAGINA DE MENSAGEM
    return render(request, 'cad_clientes_app/telaCadClientes.html', {'form': form})
