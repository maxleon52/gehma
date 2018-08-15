from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def lista_equipamentos(request):
    return render(request,'cad_equip_app/telaCadEquip.html')#MANDA A REQUISIÇÃO E O TEMPLATE (PAGINA HTML)