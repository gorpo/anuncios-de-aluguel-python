# anuncios-de-aluguel-python
Projeto open-source para anúncios de aluguel

Python 3.6.4 Django 2.0.2


<h2>Objetivo</h2>
Desenvolver aplicação para anuncios de imoveis para alugar, e com esta aplicação, aproveitando de forma simples dos recursos do Django.


<h2>Requisitos</h2>



<h2>Baixando e Rodando Aplicação</h2>

no <b>Linux:</b><br>
#clonando repositorio
git clone https://github.com/WallesonM/anuncios-de-aluguel-python.git <br>
#abrindo pasta do repositorio no terminal<br>
cd anuncios-de-aluguel-python<br>
#criando ambiente virtual do python<br>
python -m venv venv<br>
#iniciaindo ambiente virtual<br>
. venv/bin/activate<br>
#baixando e instalando django<br>
pip install django<br>
#baixando e instalando pillow <b>(obs: pillow e uma biblioca extremamente importante para funcionamento da aplicação, para trabalhar com imagens nos forms)</b><br>
pip install pillow<br>
#abrindo pasta da aplicação<br>
cd alugue<br>
#verificando se a tabelas para atualizar no banco<br>
python manage.py migrate<br>
#inciando servidor e aplicacao<br>
python manage.py runserver<br>
