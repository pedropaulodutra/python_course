# Aula 09 - Estruturando Templates: Partials, Pages e a tag `{% include %}`

Ao construir um site com Django, seus templates podem crescer bastante. Para manter seu código organizado, reutilizável e fácil de manter, usamos a divisão entre **pages** e **partials**.

---

## O que são _Partials_?

**Partials** são pedaços reutilizáveis de HTML, Eles geralmente representam componentes que se repetem nas páginas, como:

-   Cabeçalhos
-   Rodapés
-   Barras laterais
-   Cards, botões, seções, etc.

---

## O que são _Pages_?

Pages são os templates principais de cada rota do seu site, como:

-   `home.html`
-   `contato.html`
-   `sobre.html`

Essas páginas geralmente incluem vários **partials** para formar uma página completa.

---

## A tag `{% include %}`

No Django, usamos `{% include %}` para inserir um partial dentro de um template.

-   Arquivo: `templates/partials/header.html`

```html
<header>
    <h1>Meu Site</h1>
    <nav>...</nav>
</header>
```

-   Arquivo: `templates/pages/home.html`

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <title>Página Inicial</title>
    </head>
    <body>
        {% include "partials/header.html" %}

        <main>
            <h2>Bem-vindo à página inicial!</h2>
            <p>Este conteúdo é exclusivo da home.</p>
        </main>

        {% include "partials/footer.html" %}
    </body>
</html>
```

---

## Execução com `{% %}`

No Django Template Language, usamos `{% %}` para comandos e lógica de controle, por exemplo:

-   `{% include %}`: inclui outro template
-   `{% if %}`, `{% elif %}`, `{% else %}`: estruturas condicionais
-   `{% for item in lista %}`: laços de repetição
-   `{% block %}`, `{% extends %}`: herança de templates

Essas tags são **interpretadas no servidor**, e substituídas por HTML antes da resposta ser enviada ao navegador.

---

## Dica de organização de pastas:

```bash
templates/
├── namespace
│   ├── partials/
│   │   ├── header.html
│   │   ├── footer.html
│   │   └── ...
│   └── pages/
│       ├── home.html
│       ├── contato.html
│       └── ...
```
