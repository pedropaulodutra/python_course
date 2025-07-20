# Aula 12 - `STATICFILES_DIRS`: O que é?

Essa configuração no `settings.py` serve para registrar pastas adicionais onde o Django deve procurar por arquivos estáticos fora das apps.

---

## Por que isso é necessário?

Por padrão, o Django procura arquivos estáticos dentro de cada app, na subpasta chamada `static/`.

Mas às vezes você quer organizar seus arquivos estáticos em uma pasta central (fora das apps).

O Django não encontra essa pasta automaticamente. É aí que entra o `STATICFILES_DIRS`.

---

## Como configurar:

No seu `settings.py`:

```python
STATICFILES_DIRS = [
    BASE_DIR / "nome_da_pasta_de_estaticos",
]
```
