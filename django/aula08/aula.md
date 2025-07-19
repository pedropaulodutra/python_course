# Aula 08 - Entendendo a função `render()` no Django

Ao trabalhar com Django, uma das funções mais usadas nas views é a `render()`. Ela é responsável por juntar (ou renderizar) um template com os dados que queremos exibir e devolver uma resposta HTTP pronta para o navegador.

---

## Entrando na função `render`

Uma ótima dica enquanto você estuda: pressione `Ctrl` e clique em `render` no seu arquivo `views.py`. Isso te leva diretamente até o código-fonte da função no Django, esse código se encontra dentro da pasta `venv` (se você está utilizando ambientes virtuais, espero que sim). Lá você verá algo parecido com:

```python
def render(
    request, template_name, context=None, content_type=None, status=None, using=None
):
    content = loader.render_to_string(template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)
```

Mesmo que você ainda não entenda tudo, é legal ver que o `render()` é uma função Python comum. Ela recebe um request e um template obrigatóriamente, mas existem outros parâmetros que já vem setado como `None`, como o contexto, o tipo de conteúdo, o status. etc.
Ela tem a sua lógica e no final, ela usa um HttpResponse para retornar o conteúdo (como havíamos feito no início desse curso)

---

## Passando dados com o `context`

O **contexto** é um dicionário Python que envia informações do backend (sua view) para o frontend (o template). No template, você poderá usar essas informações para exibir conteúdo dinâmico.

### Exemplo

```python
from django.shortcuts import render

def home(request):
    context = {
        "name": "Pedro Dutra"
    }
    return render(request, "namespace/home.html", context)
```

Neste exemplo:

-   `request` é o objeto de requisição do Django
-   `"home.html"` é o nome do seu template
-   `"namespace"` é o nosso isolamento, que definimos anteriormente
-   `context` é um dicionário com a chave `"name"`

Agora, dentro do seu arquivo `home.html`, você pode usar essa variável com a sintaxe do Django Template Language

```html
<h1>Olá, {{ name }}!</h1>
```

O resultado será:

```html
<h1>Olá, Pedro!</h1>
```

---

## E o que está acontecendo por trás?

A função `render()` faz basicamente o seguinte:

1. Carrega o template HTML que você indicou
2. Renderiza o template substituindo variáveis como `{{ name }}` por valores do contexto
3. Retorna um **HttpResponse** com o HTML final que será enviado ao navegador
