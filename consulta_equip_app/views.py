from datetime import date, datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cad_equip_app.models import tb_equip
from cad_ordemServ_app.models import tb_historico
from cad_equip_app.forms import equipForm
from django.core.mail import send_mail


# Create your views here.

# LISTA EQUIPAMENTOS
@login_required
def listaEquip(request):
    tipoNome = request.GET.get('tipoNome', None)
    modelo = request.GET.get('modelo', None)
    numSerie = request.GET.get('numSerie', None)

    if tipoNome or modelo or numSerie:
        lista = tb_equip.objects.filter(nome__icontains=tipoNome, modelo__icontains=modelo,
                                        numSerie__icontains=numSerie)
    else:
        lista = tb_equip.objects.all()
    return render(request, 'consulta_equip_app/consultaEquip.html', {'lista': lista})


# ATUALIZA EQUIPAMENTOS
@login_required
def atualizaEquip(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    form = equipForm(request.POST or None, request.FILES or None, instance=equip)

    if form.is_valid():
        form.save()
        return redirect(
            'listaEquip')  # REDIRECIONA PARA A LISTA...MAS SERIA INTERESSANTE REDIRECIONAR PARA UM JS COM A MENSAGEM SUCESSO.

    return render(request, 'cad_equip_app/telaCadEquip.html', {'form': form})


# DELETA EQUIPAMENTOS
@login_required
def deleteEquip(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    form = equipForm(request.POST or None, request.FILES or None,
                     instance=equip)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO

    if request.method == 'POST':
        equip.delete()
        return redirect('listaEquip')

    return render(request, 'consulta_equip_app/confDeleteEquip.html', {'form': form})


def geraEmail(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    return render(request, 'consulta_equip_app/geraEmail.html', {'equip': equip})


@login_required
def enviarEmail(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    nome = equip.nome
    data = equip.proxManu.strftime('%d/%m/%Y')
    para = request.POST.get('para', None) #Variavel 'para' é o nome do campo no formulario
    send_mail(
        'TESTE ENVIO EMAIL GMAIL',
        'O equipamento %s tem uma revisão agenda para o dia %s.' % (nome, data),
        'maxleon522@gmail.com',
        [para],
        fail_silently=False,
    )
    return redirect('listaEquip')


# HISTORICO DO EQUIPAMENTO
@login_required
def historicoOs(request, id):
    hist = tb_historico.objects.filter(hEquipCod=id)
    return render(request, 'consulta_equip_app/historico.html', {'hist': hist})
