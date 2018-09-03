from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import equipForm


@login_required
def novoEquip(request):
    form = equipForm(request.POST or None, request.FILES or None)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO
    if form.is_valid():
        form.save()
        return redirect('listaEquip')  # COLOCAR PRA REDIRECIONAR PRA UMA PAGINA DE MENSAGEM
    return render(request, 'cad_equip_app/telaCadEquip.html', {'form':form})  # MANDA A REQUISIÇÃO E O TEMPLATE (PAGINA HTML)