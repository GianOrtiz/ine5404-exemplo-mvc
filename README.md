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

![UML](https://github.com/GianOrtiz/ine5404-exemplo-mvc/blob/com-mvc/UML.png?raw=true)

## Execução

Para executar este projeto, primeiro faça um git clone:

```
git clone https://github.com/GianOrtiz/ine5404-exemplo-mvc
```

Depois selecione a versão que você quiser(`sem-mvc`, `com-mvc`, `mvc-pysimplegui`, `mvc-django`), e executar o projeto com:

```python
python3 main.py
```

O usuário padrão é `default` e a senha `default`.
