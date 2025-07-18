# Aula 01 - Primeiros passos com Django

Django é um framework web de alto nível para Python que permite o desenvolvimento rápido e limpo de aplicações web.

---

## Pré-requisitos

-   Python instalado (recomenda-se versão 3.8+)
-   pip instalado (vem junto com Python)
-   Terminal / Prompt de Comando básico
-   Ambiente virtual (recomendado)

---

## Instalando o Django

Antes de tudo, crei um ambiente virtual:

```bash
python -m venv venv
```

Ative com ambiente:

-   Windows:

```bash
venv/Scripts/activate
```

-   Linux/macOS:

```bash
source venv/bin/activate
```

Instale o Django com pip:

```bash
pip install django
```

Verifique se foi instalado corretamente:

```bash
django-admin --version
```

---

## Criando o Projeto

Com o Django instalado, crie o projeto com:

```bash
django-admin startproject nome_do_projeto
```

Isso vai criar uma estrutura de pastas assim:

```bash
nome_do_projeto/
├── manage.py
└── nome_do_projeto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Acesse a pasta do projeto:

```bash
cd nome_do_projeto
```

---

## Rodando o servidor de desenvolvimento

Execute o servidor com:

```bash
python manage.py runserver
```

Você verá uma mensagem como:

```bash
Starting development server at https://127.0.0.1:8000/
```

Abra no navegador: https://127.0.0.1:8000

---

## Estrutura básica explicada

-   `manage.py`: utilitário para gerenciar o projeto
-   `settings.py`: configurações do projeto
-   `urls.py`: roteador de URLs
-   `asgi.py`/`wsgi.py`: interfaces de deploy
