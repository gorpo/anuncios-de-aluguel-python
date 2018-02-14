from django import forms
from .models import imoveis

#FORM PARA CADASTRO DE IMOVEL
class ImoveisForm(forms.ModelForm):
    class Meta:
        model = imoveis
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


