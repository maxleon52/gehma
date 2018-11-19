from cad_clientes_app.models import tb_clientes
from cad_equip_app.models import tb_equip
from cad_ordemServ_app.models import tb_os
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def menuPrincipal(request):
    dashCli = tb_clientes.objects.all().count()
    dashEquip = tb_equip.objects.all().count()
    dashOs = tb_os.objects.all().count()

    return render(request, 'menuPrincipal.html', {'dashCli': dashCli, 'dashEquip': dashEquip, 'dashOs': dashOs})


@login_required()
def my_logout(request):
    logout(request)
    return redirect('login')


def notificacao(request, dataCad, dataHoje):
    noti = tb_equip.objects.all()
    dataCad = datetime.strptime(tb_equip.proxManu, "%d-%m-%Y")
    dataHoje = datetime.today()
    return abs(noti(dataCad - dataHoje).days)