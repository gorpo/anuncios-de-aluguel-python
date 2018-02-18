from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Imoveis
from .forms import ImoveisForm
from django.contrib.auth.decorators import login_required


# listagem de imoveis
def home(request):
    listaImoveis = Imoveis.objects.all()
    return render(request, 'imoveis.html', {'listaImoveis':listaImoveis})

@login_required
def cadastroImoveis(request):
    form = ImoveisForm()
    mensagem  = 'Cadastrado com sucesso!'
    if request.method == "POST":
        form = ImoveisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(
                'Imovel cadasrado com sucesso!'
                '<br>'
                '<a href="/">Voltar</a>')
    return render(request, 'cadastroimoveis.html', {'form': form})

def buscarCep(request):
    buscar = request.POST['cep']
    listaImoveis = Imoveis.objects.filter(cep__contains=buscar)
    return render(request, 'busca.html', {'listaImoveis':listaImoveis})






