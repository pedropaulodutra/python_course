# Aula 03 - Introdução às URLs no Django

No Django, as URLs (Uniform Resource Locators) são usadas para **mapear endereços da web** para **funções que retornam respostas**. Essas funções são chamadas de **views**.

Imagine: quando alguém acessa `seusite.com/sobre`, o Django precisa saber **o que mostrar**, é isso que as URLs fazem!

---

## O arquivo `urls.py`

Quando você cria um projeto Django, o Django gera um arquivo chamado `urls.py` dentro da pasta do projeto. Ele é o ponto de entrada para o roteamento de URLs.

Por padrão o arquivo de urls do seu projeto vem assim:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls) # <- o primeiro argumento é a rota, o segundo a view.
]
```

Com intuito de exemplificar, criaremos uma rota e uma view dentro do arquivo `urls.py`

> ⚠️ IMPORTANTE: Isso está errado!!!
> Colocar views diretamente dentro do `urls.py` não é uma boa prática e não será feito em projetos reais, usaremos essa abordagem apenas como exemplo para simplificar enquanto ainda não criamos nossos próprios apps.

```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('<h1>Sobre</h1>')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sobre/", my_view)
]
```

### O que acontece aqui?

-   O Django procura pelas **rotas** definidas na lista `urlpatterns`.
-   Ao acessar `http://localhost:8000/sobre/`, o Django verifica que essa URL corresponde ao caminho `"sobre/"` definido no `path(...)`.
-   Quando encontra a correspondência, ele **executa a função** associada a essa rota, neste caso, `my_view`.
-   A função `my_view(request)` **recebe automaticamente o objeto `request`** como argumento, pois é assim que o Django envia as requisições para as views.
-   Dentro da `my_view`, utilizamos `HttpResponse(...)` para **retornar uma resposta HTTP válida**, que neste exemplo é um simples HTML: `<h1>Sobre</h1>`.

---

## Testando

Para testar, precisamos iniciar o servidor de testes:

```bash
python manage.py runserver
```

após isso, acesse seu navegador no endereço http://localhost:8000/sobre/ e você irá ver a tag que utilizamos no argumento do retorno da função `my_view`.

> Verifique se o django iniciou o servidor na porta 8000 no seu console caso você não consiga acessar
