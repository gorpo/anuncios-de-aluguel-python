from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



#REGISTRO DE USUARIO
def register(request):
    template_name = 'contas/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                'Usuario cadasrado com sucesso!'
                '<br>'
                'Volte para realizar login!'
                '<a href="/contas/">Voltar</a>')
    else:
        form = UserCreationForm()

    context = {
        'form': UserCreationForm()
    }
    return render(request, template_name, context)

#DASHBOARD DO USUARIO
@login_required
def dashboard(request):

    return render(request, 'contas/dashboard.html')