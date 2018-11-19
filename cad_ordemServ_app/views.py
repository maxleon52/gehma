from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from cad_clientes_app.models import tb_clientes
from cad_equip_app.models import tb_equip
from cad_ordemServ_app.models import tb_os, tb_historico
from cad_clientes_app.forms import clienteForm
from cad_equip_app.forms import equipForm
from cad_ordemServ_app.forms import OsForm, OsEditForm
from django.views.generic import TemplateView
from django.core import serializers

# Create your views here.
# LISTAR ORDEM DE SERVIÇOS e GERAR O FORM DE O.S.

# LISTA ORDEM DE SERVIÇO
from django_xhtml2pdf.utils import generate_pdf


@login_required
def listaOrdemServico(request):
    numOs = request.GET.get('numOs', None)
    nome = request.GET.get('nome', None)
    cnpj = request.GET.get('cnpj', None)
    cpf = request.GET.get('cpf', None)

    if numOs or nome or cnpj or cpf:
        lista = tb_os.objects.filter(cod__icontains=numOs, cliNome__icontains=nome, cliCnpj__icontains=cnpj,
                                     cliCpf__icontains=cpf)
    else:
        lista = tb_os.objects.all()

    return render(request, 'cad_ordemServ_app/listaOs.html', {'lista': lista})


# ATUALIZA ORDEM DE SERVIÇO
@login_required
def atualizaOs(request, id):
    os = get_object_or_404(tb_os, pk=id)
    form = OsEditForm(request.POST or None, request.FILES or None, instance=os)

    if form.is_valid():
        form.save()
        return redirect(
            'listaOrdemServico_urls')  # REDIRECIONA PARA A LISTA...MAS SERIA INTERESSANTE REDIRECIONAR PARA UM JS COM A MENSAGEM SUCESSO.

    return render(request, 'cad_ordemServ_app/editOs.html', {'form_os': form})


# DELETA ORDEM DE SERVIÇO
@login_required
def deleteOs(request, id):
    os = get_object_or_404(tb_os, pk=id)
    form = OsForm(request.POST or None, request.FILES or None,
                  instance=os)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO

    if request.method == 'POST':
        os.delete()
        return redirect('listaOrdemServico_urls')

    return render(request, 'cad_ordemServ_app/confDeleteOs.html', {'form': form, 'os': os})


# LISTAR CLIENTES
@login_required
def lista_clientes_os(request):
    lista = tb_clientes.objects.all()  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL
    return render(request, 'cad_ordemServ_app/listaCliente_os.html',
                  {'lista': lista})  # MOSTRANDO O TEMPLATE E A CONSULTA NO BANCO


# LISTAR EQUIPAMENTOS
@login_required
def lista_Equip_os(request):
    lista = tb_equip.objects.all()  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL
    return render(request, 'cad_ordemServ_app/listaEquip.html',
                  {'lista': lista})  # MOSTRANDO O TEMPLATE E A CONSULTA NO BANCO


# SELECIONA CLIENTES NA TELA DE OS
@login_required
def SelecClientes_os(request, id):
    cliente = get_object_or_404(tb_clientes, pk=id)
    # request.session['cliente'] = serializers.serialize('json', [cliente])
    formCli = clienteForm(request.POST or None, request.FILES or None, instance=cliente)

    return render(request, 'cad_ordemServ_app/telaCadOrdemServ.html', {'formCli': formCli})


# SELECIONA EQUIPAMENTOS NA TELA DE OS
@login_required
def SelecEquip_os(request, id):
    equip = get_object_or_404(tb_equip, pk=id)
    # cliente = serializers.deserialize('json', request.session['cliente'])
    # cliente = request.session['cliente']
    # print(cliente)
    # formCli = clienteForm(None, None, instance=cliente)
    formEquip = equipForm(request.POST or None, request.FILES or None, instance=equip)

    return render(request, 'cad_ordemServ_app/telaCadOrdemServ.html', {'formEquip': formEquip})


# REDIRECIONA PRA GERAR UMA NOVA OS
@login_required
def novaOS(request):
    return render(request, 'cad_ordemServ_app/os.html')


# antiga função de gerar os forms na tela

# cliente = get_object_or_404(tb_clientes, pk=id)
# formCli = clienteForm(request.POST or None, request.FILES or None, instance=cliente)
# equip = get_object_or_404(tb_equip, pk=id)
# formEquip = equipForm(request.POST or None, request.FILES or None, instance=equip)

# return render(request, 'cad_ordemServ_app/os.html', {cliente}, {equip})#{'formCli': formCli}, {'formEquip': formEquip})

class CreateOs(TemplateView):
    template_name = 'cad_ordemServ_app/cadOs.html'

    def get_context_data(self, **kwargs):
        context = super(CreateOs, self).get_context_data(**kwargs)
        context['clients'] = tb_clientes.objects.all()
        context['equips'] = tb_equip.objects.all()
        context['form_os'] = OsForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form_os = context['form_os']
        if form_os.is_valid():
            os = form_os.save(commit=False)
            client = get_object_or_404(tb_clientes, pk=self.request.POST['client'])
            equip = get_object_or_404(tb_equip, pk=self.request.POST['equip'])
            os.cliCod = client
            os.cliNome = client.nome
            os.cliCep = client.cep
            os.cliContato = client.contato
            os.cliEndereco = client.endereco
            os.cliBairro = client.bairro
            os.cliCidade = client.cidade
            os.cliUf = client.uf
            os.cliCnpj = client.cnpj
            os.cliCpf = client.cpf
            os.equipCod = equip
            equip.proxManu = os.equipProxManu
            os.status = str("ABERTO")
            os.save()
            equip.save()
            # Historico
            tb_historico.objects.create(
                histReclamado=os.defReclamado,
                hConstatado=os.defConstatado,
                hServRealizado=os.ServRealizado,
                hEquipCod=os.equipCod,
                hOsCod=os
            )

            return redirect('listaOrdemServico_urls')


# Django-xhtml2pdf
@login_required
def pdf_rel_assisTec(request, id):
    os = get_object_or_404(tb_os, pk=id)

    return render(request, 'cad_ordemServ_app/pdf_rel_assisTec.html', {'os': os})


# FINALIZA ou REABRE OS
def finalizaOs(request, id):
    os = get_object_or_404(tb_os, pk=id)
    if str(os.status) == str('ABERTO'):
        os.status = str('FINALIZADO')
        os.save()
        return redirect('listaOrdemServico_urls')
    elif str(os.status) == str('FINALIZADO'):
        os.status = str('ABERTO')
        os.save()
        return redirect('listaOrdemServico_urls')
    else:
        return redirect('listaOrdemServico_urls')
