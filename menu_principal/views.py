from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def menuPrincipal(request):
    return render(request, 'menuPrincipal.html')

@login_required()
def my_logout(request):
    logout(request)
    return redirect('login')