# Aula 07 - Templates no Django: renderização, organização e namespaces

Templates no Django são arquivos HTML dinâmicos, onde podemos usar **variáveis** e **lógica** do Django com a sintaxe de template tags (`{{ }}` e `{% %}`).

Eles são usados para separar a **lógica Python** da **interface HTML**

---

## Estrutura de diretórios

É recomendado criar um diretório chamado `templates` dentro de cada app. Exemplo:

```bash
meu_projeto/
│
├── meu_app/
│ └── templates/
│     └── index.html
```

---

## Usando o `render()`

A função `render()` é usada para juntar um template HTML com uma requisição HTTP e retornar isso como resposta.

Antes, usávamos `HttpResponse`, mas com `render` o Django trata tudo para nós:

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

> Em breve, vamos aprender a usar o contexto com render() para enviar dados do Python para o HTML.

---

## O Django encontra os templates sozinho?

Quase. O Django só procura templates em apps registrados no `INSTALLED_APPS` ou nas pastas listadas manualmente na configuração `DIRS`.

Por padrão, em settings.py você verá:

```python
INSTALLED_APPS = [
    ...
]
```

Se seu app não estiver listado aqui, o Django não encontrará seus templates.

---

## Como saber o nome do seu app?

Dentro da pasta do app, no arquivo `apps.py`, veja a classe que herda `AppConfig`. Lá estará:

```python
class MeuAppConfig(AppConfig):
    name = 'meu_app'
```

Usa esse nome ao adicionar no `INSTALLED_APPS`.

---

## Criando um diretório global de templates

É comum criar uma pasta de templates "globais", fora dos apps, chamada `base_templates`. Para que o Django saiba buscá-la, vá até `TEMPLATES` em `settings.py` e edite assim:

```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'base_templates'],
        ...
    },
]
```

> BASE_DIR já vem pronto no início de settings.py. Ele aponta para a raiz do projeto:

```python
BASE_DIR = Path(__file__).resolve().parent.parent
```

---

## Colisão de nomes

Se você tiver um `home.html` em `base_templates` e outro em `meu_app/templates`, o Django pode pegar o errado, pois ele busca na ordem dos diretórios definidos.

---

## Usando namespaces para evitar conflitos

Uma boa prática é criar subpastas com o nome do app dentro de `templates`. Assim, você evita colisões.
Exemplo de estrutura:

```bash
meu_projeto/
│
├── base_templates/
│   └── global/
│       └── home.html
│
├── meu_app/
│   └── templates/
│       └── meu_app/
│           └── home.html

```

E na view:

```python
from django.shortcuts import render

def home(request):
    return render(request, "meu_app/home.html")
```

Dessa forma, você deixa claro qual template está sendo usado e mantém o projeto organizado.
