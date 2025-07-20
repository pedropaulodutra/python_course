# Aula 11 - Adicionando Static Files para CSS

Para que o Django consiga localizar seus arquivos estáticos durante o desenvolvimento, precisamos garantir algumas configurações que já são inseridas no arquivo `settings.py` do projeto.

---

## `django.contrib.staticfiles` no `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'django.contrib.staticfiles'
]
```

Essa é uma app interna do Django que cuida da gestão dos arquivos estáticos do seu projeto, como CSS, JavaScript, imagens e fontes.

### Por que isso importa?

Ao deixar `django.contrib.staticfiles` na lista de `INSTALLED_APPS`, você está dizendo ao Django:

"Quero que o sistema de arquivos estáticos esteja ativo. Quero poder usar `{% static %}`, `collectstatic`, e servir arquivos durante o desenvolvimento."

Se você remover essa app, o Django não conseguirá encontrar e servir seus arquivos estáticos automaticamente.

---

## O que é `STATIC_URL`?

Essa variável define a URL base onde os arquivos estáticos serão servidos no navegador.

```python
STATIC_URL = '/static/'
```

### Exemplo

Se você tiver um arquivo chamado style.css em:

```bash
meu_app/
├── static/
│   └── namespace/
│       └── css/
│           └── style.css
```

E fizer isso no template:

```html
<link rel="stylesheet" href="{% static 'namespace/css/style.css' %}" />
```

O Django vai gerar algo assim:

```html
<link rel="stylesheet" href="/static/namespace/css/style.css" />
```

Ou seja, o navegador vai tentar acessar:

```bash
http://localhost:8000/static/namespace/css/style.css
```

---

## Mas atenção

Antes de usá-la, você precisa carregar o recurso no topo do seu template com:

```django
{% load static %}
```
