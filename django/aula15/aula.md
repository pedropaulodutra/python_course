# Aula 15 - Herença de Templates no Django

A herança de templates permite reutilizar HTML, criando uma estrutura base que será estendida por outras páginas. Isso evita duplicação de código.

---

## Exemplo de estrutura:

```bash
templates/
│
├── base.html       ← Template base
├── home.html       ← Herda de base.html
└── contato.html    ← Herda de base.html
```

### `base.html` - Estrutura principal

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8" />
        <title>{% block title %}Minha Página{% endblock %}</title>
    </head>
    <body>
        <header>
            <h1>Site Exemplo</h1>
        </header>

        <main>
            {% block content %}
            <!-- Conteúdo específico de cada página -->
            {% endblock %}
        </main>

        <footer>
            <p>Rodapé do site</p>
        </footer>
    </body>
</html>
```

### `home.html` - Herda da base

```html
{% extends "base.html" %} {% block title %}Página Inicial{% endblock %} {% block
content %}
<h2>Bem-vindo ao site!</h2>
<p>Essa é a página inicial.</p>
{% endblock %}
```

### `contato.html` - Também herda da base

```html
{% extends "base.html" %} {% block title %}Contato{% endblock %} {% block
content %}
<h2>Fale conosco</h2>
<form>
    <!-- formulário aqui -->
</form>
{% endblock %}
```

---

## O que são `blocks`?

-   `{% block nome %}` define pontos onde os filhos injetam conteúdo.
-   É obrigatório abrir e fechar: `{% block content %} {% endblock content %}`

---

## Vantagens

-   Reutilização da estrutura
-   Organização e clareza
-   Manutenção mais fácil
