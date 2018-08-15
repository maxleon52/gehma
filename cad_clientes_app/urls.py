from django.urls import path
from .views import novoCliente

urlpatterns = [
    path('novoClientes/', novoCliente, name='novoCliente'), #caminho(APP) e função na view

]