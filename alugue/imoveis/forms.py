from django import forms
from .models import Imoveis

#FORM PARA CADASTRO DE IMOVEL
class ImoveisForm(forms.ModelForm):
    class Meta:
        model = Imoveis
        fields = [

            'nome',
            'endereco',
            'complemento',
            'numero',
            'cep',
            'valor',
            'telefone',
            'email',
            'descricao',
            'image',
        ]


