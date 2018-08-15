from django.urls import path
from .views import menuPrincipal, my_logout

urlpatterns = [
    path('', menuPrincipal, name="menuPrincipal_urls"),
    path('logout/', my_logout, name="logout")

]