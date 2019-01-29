import client as client
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cad_clientes_app.models import tb_clientes
from .forms import equipForm, orcamentosForm


@login_required
def novoEquip(request):
    clientes = tb_clientes.objects.all()
    form = equipForm(request.POST or None, request.FILES or None)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO
    if form.is_valid():
        #os = form.save(commit=False)
        #client = get_object_or_404(tb_clientes, pk=request.POST['client'])
        #os.cliCod = client
        form.save()
        return redirect('listaEquip')  # COLOCAR PRA REDIRECIONAR PRA UMA PAGINA DE MENSAGEM
    return render(request, 'cad_equip_app/telaCadEquip.html', {'form':form,'clientes':clientes})  # MANDA A REQUISIÇÃO E O TEMPLATE (PAGINA HTML)


def orcamentos(request):
    return render(request,'cad_equip_app/orcamentos.html')

def novoOrcamento(request):
    form = orcamentosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orcamentos_urls')
    return render(request, 'cad_equip_app/novoOrcamento.html', {'form':form})