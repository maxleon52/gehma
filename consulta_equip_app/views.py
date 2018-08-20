from django.shortcuts import render, redirect, get_object_or_404
from cad_equip_app.models import tb_equip
from cad_equip_app.forms import equipForm
# Create your views here.

#LISTA EQUIPAMENTOS
def listaEquip(request):
    lista = tb_equip.objects.all()
    return render(request, 'consulta_equip_app/consultaEquip.html',{'lista':lista})

#ATUALIZA EQUIPAMENTOS
def atualizaEquip(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    form = equipForm(request.POST or None, request.FILES or None, instance=equip)

    if form.is_valid():
        form.save()
        return redirect('listaEquip')  # REDIRECIONA PARA A LISTA...MAS SERIA INTERESSANTE REDIRECIONAR PARA UM JS COM A MENSAGEM SUCESSO.

    return render(request, 'cad_equip_app/telaCadEquip.html', {'form': form})

#DELETA EQUIPAMENTOS
def deleteEquip(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    form = equipForm(request.POST or None, request.FILES or None, instance=equip)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO

    if request.method == 'POST':
        equip.delete()
        return redirect('listaEquip')

    return render(request, 'consulta_equip_app/confDeleteEquip.html', {'form': form})