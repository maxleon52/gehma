from cad_clientes_app.forms import clienteForm
from cad_clientes_app.models import tb_clientes
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django_xhtml2pdf.utils import generate_pdf, pdf_decorator


# CONSULTA CLIENTES
@login_required
def lista_clientes(request):
    razNome = request.GET.get('razNome', None)
    cnpj = request.GET.get('cnpj', None)
    cpf = request.GET.get('cpf', None)

    if razNome or cnpj or cpf:
        lista = tb_clientes.objects.filter(nome__icontains=razNome, cnpj__icontains=cnpj,
                                           cpf__icontains=cpf)  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL
    else:
        lista = tb_clientes.objects.all()  # CONSULTA NO MODEL (BD) E ARMAZENA NA VARIAVEL

    return render(request, 'consulta_clientes_app/consultaClientes.html',
                  {'lista': lista})  # MOSTRANDO O TEMPLATE E A CONSULTA NO BANCO


# METODO QUE REDIRECIONA A PAGINA e GERA O FORM NA TELA
# CADASTRA NOVO CLIENTE
@login_required
def novoCliente(request):
    form = clienteForm(request.POST or None,
                       request.FILES or None)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'cad_clientes_app/telaCadClientes.html', {'form': form})


# ATUALIZA CLIENTES
@login_required
def atualizaCliente(request, id):
    cliente = get_object_or_404(tb_clientes, pk=id)
    form = clienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect(
            'lista_clientes')  # REDIRECIONA PARA A LISTA...MAS SERIA INTERESSANTE REDIRECIONAR PARA UM JS COM A MENSAGEM SUCESSO.

    return render(request, 'cad_clientes_app/telaCadClientes.html', {'form': form})


# DELETA CLIENTE
@login_required
def deleteCliente(request, id):
    cliente = get_object_or_404(tb_clientes, pk=id)
    form = clienteForm(request.POST or None, request.FILES or None,
                       instance=cliente)  # REQUEST.POST MANDA PARA O BANCO...REQUEST.FILES MANDA OS ASQUIVOS DE MIDIA, POREM NO HTML DEVE TER O ENCTYPER PREENCHIDO

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')

    return render(request, 'consulta_clientes_app/confDeleteCliente.html', {'form': form})


#Django-xhtml2pdf
#@pdf_decorator
def pdf_generation_cliente(request, id):
    #resp = HttpResponse(content_type='application/pdf')
    #result = generate_pdf('cad_clientes_app/teste.html', file_object=resp)
    #return result
    cliente = get_object_or_404(tb_clientes, pk=id)

    #form = clienteForm(request.POST or None, request.FILES or None, instance=cliente)

    return render(request, 'cad_clientes_app/teste.html', {'form':cliente})
