from django.shortcuts import render, get_object_or_404, redirect
from cad_clientes_app.models import tb_clientes
from cad_equip_app.models import tb_equip
from cad_clientes_app.forms import clienteForm
from cad_equip_app.forms import equipForm
from cad_ordemServ_app.forms import OsForm

from django.core import serializers


# Create your views here.
# LISTAR ORDEM DE SERVIÇOS e GERAR O FORM DE O.S.


def listaOrdemServico(request):
    formOs = OsForm(request.POST or None, request.FILES or None)
    if formOs.is_valid():
        formOs.save()
    return render(request, 'cad_ordemServ_app/telaCadOrdemServ.html', {'formOs': formOs})

# LISTAR CLIENTES
def lista_clientes_os(request):
    lista = tb_clientes.objects.all()  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL
    return render(request, 'cad_ordemServ_app/listaCliente_os.html',{'lista': lista})  # MOSTRANDO O TEMPLATE E A CONSULTA NO BANCO

# LISTAR EQUIPAMENTOS
def lista_Equip_os(request):
    lista = tb_equip.objects.all()  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL
    return render(request, 'cad_ordemServ_app/listaEquip.html',{'lista': lista})  # MOSTRANDO O TEMPLATE E A CONSULTA NO BANCO

# SELECIONA CLIENTES NA TELA DE OS
def SelecClientes_os(request, id):
    cliente = get_object_or_404(tb_clientes, pk=id)
    #request.session['cliente'] = serializers.serialize('json', [cliente])
    formCli = clienteForm(request.POST or None, request.FILES or None, instance=cliente)

    return render(request, 'cad_ordemServ_app/telaCadOrdemServ.html', {'formCli': formCli})

# SELECIONA EQUIPAMENTOS NA TELA DE OS
def SelecEquip_os(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    #cliente = serializers.deserialize('json', request.session['cliente'])
    # cliente = request.session['cliente']
    #print(cliente)
    # formCli = clienteForm(None, None, instance=cliente)
    formEquip = equipForm(request.POST or None, request.FILES or None, instance=equip)

    return render(request, 'cad_ordemServ_app/telaCadOrdemServ.html', {'formEquip': formEquip})

#REDIRECIONA PRA GERAR UMA NOVA OS
def novaOS(request):
    return render(request, 'cad_ordemServ_app/os.html')

#antiga função de gerar os forms na tela

    #cliente = get_object_or_404(tb_clientes, pk=id)
    #formCli = clienteForm(request.POST or None, request.FILES or None, instance=cliente)
    #equip = get_object_or_404(tb_equip, pk=id)
    #formEquip = equipForm(request.POST or None, request.FILES or None, instance=equip)

    #return render(request, 'cad_ordemServ_app/os.html', {cliente}, {equip})#{'formCli': formCli}, {'formEquip': formEquip})