from django.urls import path
from .views import novoEquip

urlpatterns = [
    path('novoEquip/', novoEquip, name='novoEquip_urls'), #caminho(APP) e função na view
]
