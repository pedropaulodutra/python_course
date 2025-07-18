# Aula 05 - Criando e Conhecendo Apps no Django

No Django, um **projeto** é como o contêiner principal e **apps** são os módulos responsáveis por funcionalidades específicas (ex: blog, loja, contas, etc).

---

## Criando um App

Dentro do diretório do seu projeto Django, rode o seguinte comando no terminal:

```bash
python manage.py startapp nome_do_app
```

Isso criará uma nova pasta com a estrutura básica de um app Django.

---

## Estrutura Básica de um App

```bash
nome_do_app/
    │
    ├── __init__.py
    ├── admin.py         # Registra modelos no painel administrativo
    ├── apps.py          # Configuração do app
    ├── migrations/      # Arquivos de migração do banco de dados
    │   └── __init__.py
    ├── models.py        # Modelos (tabelas do banco de dados)
    ├── tests.py         # Testes automatizados
    └── views.py         # Funções ou classes que processam requisições
```
