# Aula 06 - Conhecendo Melhor Apps no Django

Como havíamos falado anteriormente, um projeto é como um contêiner principal e apps são os módulos responsáveis por funcionalidades específicas

Você pode criar um arquivo chamado `urls.py` dentro do **app** para criar outras rotas a partir daquele app

---

## Criando `urls.py` no App

Crie manualmente um arquivo chamado `urls.py` dentro do seu app, bem parecido com o `urls.py` já fornecido na estrutura inicial:

```python
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

urlpatterns = [
    path("", home)
]
```

---

## Usando `include` no Projeto Principal

No arquivo `urls.py` do seu projeto principal, você precisa usar a função `include()` para conectar as rotas do app:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include("nome_do_app.urls"))
]
```

Isso quer dizer que qualquer rota definida no `nome_do_app/urls.py` agora estará acessível a partir do caminho `/home/`

---

## Por que usar `include()`?

-   Permite dividir rotas por app, mantendo o projeto organizado.
-   Facilita o reaproveitamento de apps.
-   Evita que o `urls.py` principal fique gigante.

---

## Deixando o Projeto mais Profissional

Agora que incluímos as urls vindas do app, devemos separar o que são views de urls, e o Django já cria em sua estrutura inicial do app, um arquivo chamado `views.py`, onde justamente podemos mover a nossa função que é chamada no segundo argumento da função `path()`

### Criando as views

De acordo com a estrutura do nosso projeto, o arquivo `views.py` deverá ficar dessa forma:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1>")
```

### Importando o `views.py` no `urls.py`

No `urls.py` do seu app, você agora deverá chamar a view vindo do local correto, ficando assim:

```python
from django.urls import path
from nome_do_app.views import home

urlpatterns = [
    path("", home)
]
```

Agora qualquer rota que você criar dentro do seu app, terá a url `/home/nome_da_sua_rota`
