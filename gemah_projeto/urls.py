"""gemah_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from menu_principal import urls as menuPrincipal_urls              #A PONTA PARA O ARQUIVO URLS DO APP
from cad_clientes_app import urls as CadClientesAppUrls              #A PONTA PARA O ARQUIVO URLS DO APP
from cad_equip_app import urls as CadEquipAppUrls                    #A PONTA PARA O ARQUIVO URLS DO APP
from consulta_clientes_app import urls as cadConsultaCliAppUrls         #A PONTA PARA O ARQUIVO URLS DO APP
from consulta_equip_app import urls as cadConsultaAppEquipUrls         #A PONTA PARA O ARQUIVO URLS DO APP
from cad_ordemServ_app import urls as cadOrdemServAppUrls

urlpatterns = [
    path('', include(menuPrincipal_urls)),                           #CAIU NO ADMIN
    path('admin/', admin.site.urls),                                 #CAIU NO ADMIN
    path('cad_clientes_app/', include(CadClientesAppUrls)),          #caminho(APP) e função na view
    path('cad_equip_app/', include(CadEquipAppUrls)),                #caminho(APP) e função na view
    path('consulta_clientes_app/', include(cadConsultaCliAppUrls)),     #caminho(APP) e caminho da URL no arquivo de urls da APP
    path('consulta_equip_app/', include(cadConsultaAppEquipUrls)),     #caminho(APP) e caminho da URL no arquivo de urls da APP
    path('ordemServico/', include(cadOrdemServAppUrls)),     #caminho(APP) e caminho da URL no arquivo de urls da APP
    path('login/', auth_views.LoginView.as_view(), name='login'),    #VAI NA PASTA REGISTRATION E BUSCA A PAGINA DE LOGIN

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
