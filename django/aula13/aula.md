# Aula 13 - `STATIC_ROOT` e `collectstatic`

## O que é `STATIC_ROOT`?

É o caminho absoluto da pasta onde o Django vai juntar todos os arquivos estáticos quando você rodar o comando:

```bash
python manage.py collectstatic
```

---

## Quando é usado?

Somente em produção.
Durante o desenvolvimento, o Django serve os arquivos diretamente das pastas `static/` de cada app ou dos caminhos definidos em `STATICFILES_DIRS`.

Já na produção, é mais eficiente (e recomendado) copiar tudo para uma única pasta, definida em `STATIC_ROOT`, para que o servidor (Nginx, Apache etc.) consiga servir esses arquivos de forma otimizada.

---

## Como configurar?

No seu `settings.py`, de preferência perto das configurações dos arquivos estáticos, coloque:

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

> ⚠️ Repare que agora temos duas coisas: `STATIC_URL` (a URL usada nos templates) e `STATIC_ROOT` (a pasta onde os arquivos serão colocados após o collectstatic).

Depois de configurar o `STATIC_ROOT`, execute:

```bash
python manage.py collectstatic
```

O Django vai:

-   Buscar arquivos estáticos em todas as apps e diretórios definidos.
-   Copiar tudo para a pasta definida em `STATIC_ROOT` (no exemplo, `staticfiles/`).
