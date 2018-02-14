# anuncios-de-aluguel-python
Projeto open-source para anúncios de aluguel

Python 3.6.4 Django 2.0.2


<h2>Objetivo</h2>
Desenvolver aplicação para anuncios de imoveis para alugar, e com esta aplicação, aproveitando de forma simples dos recursos do Django.


<h2>Requisitos</h2>
Criar interface amigavel ao usuario, onde os anuncios devem ser criados nao atravez da plataforma "admin", mas sim atraves de usuarios cadastrados;<br>
Realizar a listagem de imoveis cadastrados, e disponibilixar barra de pesquisa por CEP, facilitando encontrar imoveis mais proximos;<br>
Inserir imagens ao cadastrar os imoveis para facilitar a visualização dos mesmos<br>


<h2>Baixando e Rodando Aplicação</h2>

no <b>Linux:</b><br>
#clonando repositorio
git clone https://github.com/WallesonM/anuncios-de-aluguel-python.git <br>

#abrindo pasta do repositorio no terminal<br>
cd anuncios-de-aluguel-python<br>

#criando ambiente virtual do python<br>
python3 -m venv venv<br>

#iniciaindo ambiente virtual<br>
. venv/bin/activate<br>

#baixando e instalando django<br>
sudo pip install Django==2.0.2<br>

#baixando e instalando pillow <b>(obs: pillow e uma biblioca extremamente importante para funcionamento da aplicação, para trabalhar com imagens nos forms)</b><br>
sudo pip install pillow<br>

#abrindo pasta da aplicação<br>
cd alugue<br>

#verificando se a tabelas para atualizar no banco<br>
python3 manage.py migrate<br>

#inciando servidor e aplicacao<br>
python3 manage.py runserver<br>

<a href="http://localhost:8000/">localhost:8000</a>

<h2>Se cadastrando e anunciando</h2>

Clique na opção "Entre p/ Anunciar"<br>
logo abaixo vera a opção "Cadastrar", e entrar em um fomulario, neste formulario <b>sua senha devera ter letras e numeros</b>,<br>

após concluido clieque na opção "voltar", e efetue login com seu usuario e senha cadastrados...<br>
voce sera redirecionado ao "Dashboard", onde tera a opçao de criar um anuncio, preenche os campos e clique em salvar.<br>

logo após vera seu anuncio na listagem inicial! :)

