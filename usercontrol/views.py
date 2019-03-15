from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as django_login

from .sca_api import Authenticator


def login(request):
    status = 200

    if request.method == 'POST':
        usuario = Authenticator().authenticate(request,
                                               request.POST.get('username', ''), 
                                               request.POST.get('password', ''))

        if usuario:
            django_login(request, usuario)
            return redirect('admin:index')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Usuário ou Senha inválidos')
            status = 403

    return render(request, 'usercontrol/login.html', status=status)
