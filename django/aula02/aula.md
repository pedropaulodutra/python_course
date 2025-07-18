# Aula 02 - Entendendo os Arquivos Iniciais de um Projeto Django

Ao rodar o comando:

```bash
django-admin startproject nome_do_projeto .
```

Você verá uma estrutura assim:

```bash
├── manage.py
├── meu_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

## `manage.py`

-   Arquivo de utilidade para interagir com o Django
-   Permite rodar comandos como:

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp minha_app
```

---

## `nome_do_projeto` (diretório interno)

Contém as configurações principais do seu projeto

-   `init.py`
    -   Torna esse diretório um pacote Python
    -   Geralmente fica vazio
-   `settings.py`
    -   Onde ficam todas as configurações do projeto
    -   Aplicações instaladas
    -   Banco de dados
    -   Idioma, fuso horário
    -   Diretórios de arquivos estáticos e templates
-   `urls.py`
    -   Configuração para ASGI (servidores assíncronos)
    -   Usado para aplicações em tempo real como WebSockets.
-   `wsgi.py`
    -   Configuração para WSGI (servidores síncronos)
    -   Usado na maioria dos servidores de produção tradicionais
