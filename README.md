# Estoque MVC

Projeto de demonstração de MVC para controle de um estoque qualquer.

O projeto consiste de quatro "branches" diferentes:

- `sem-mvc`: projeto sem MVC executando em uma aplicação de linha de comando;
- `com-mvc`: projeto com MVC executando em uma aplicação de linha de comando;
- `mvc-pysimplegui`: projeto com MVC executando visualmente com PySimpleGUI, é o mesmo que este branch master;
- `mvc-django`: projeto com MVC([MTC](https://stackoverflow.com/questions/6621653/django-vs-model-view-controller#answer-6622043)) utilizando o framework Django para web.

## Descrição

Como controle de estoque subentende-se que para acessar o sistema seja necessário um usuário com nome e senha. O estoque contem produtos quaisquer com suas quantidades, que podem ser retiradas ou repostas.

## Diagrama de Classes

![UML](https://github.com/GianOrtiz/ine5404-exemplo-mvc/blob/mvc-django/UML.png?raw=true)

## Execução

Para executar este projeto, é necessário ter `django` instalado e `sqlite3`, que é o banco de dados utilizado.

- [Link para instalação do django](https://docs.djangoproject.com/en/3.2/intro/install/)
- [Link para instalação do sqlite3](https://www.sqlite.org/download.html)

```
git clone https://github.com/GianOrtiz/ine5404-exemplo-mvc
```

Antes de executar o django, precisamos realizar as migrações para o sqlite3:

```
python3 manage.py migrate
```

Agora para executar o projeto django é preciso executar o seguinte comando:

```
python3 manage.py runserver
```

Que irá executar um servidor em `http://localhost:8000`.

As seguintes páginas estão disponíveis:

- `/`: lista dos produtos no sistema;
- `/accounts/login`: login do usuário;
- `/admin`: painel de administração;
- `products/add`: adiciona novo produto;
- `products/:id/detail`: detalhes de um produto;
- `products/:id/delete`: remoção de um produto;
- `products/:id/update`: atualiza informações de um produto;

Antes de logar talvez seja necessário criar um usuário para admin, basta executar o comando:

```
python3 manage.py createsuperuser
```

Este usuário pode ser utilizado tanto para logar no sistema através de `/` ou `/accounts/login`, quanto utilizar o painel de administração.
