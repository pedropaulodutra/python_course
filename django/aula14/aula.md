# Aula 14 - URLs no Django

Django usa o sistema de roteamento para associar URLs a views.

O arquivo principal geralmente é `urls.py`, e nele usamos a função `path()`.

---

## URLs com `<argumentos>`

Você pode capturar partes da URL dinamicamento com _path converters_:

```python
path('suaurl/<id>', views.suaview)
```

Porém ao acessar o endereço e tentar passar o id, você verifica que sua função recebeu mais argumentos do que o esperado.

Você deve preparar sua função para receber esse argumento

### E os path converters?

Você pode capturar valores dinâmicos diretamente da URL. Isso é feito usando os chamados path converters, como:

-   `<str:nome>`: captura uma string (sem barras)
-   `<int:id>`: captura um número inteiro
-   `<slug:slug>`: captura strings que podem conter hífens, ideal para URLs amigáveis
-   `<uuid:uid>`: captura um UUID
-   `<path:algo>`: captura uma string que pode incluir barras

Exemplo:

```python
urlpatterns = [
    path('suaurl/<int:codigo>/', views.suaview)
]
```

```python
def suaview(request, codigo):
    return HttpResponde(f"Produto com código: {codigo}")
```

Ao acessar `suaurl/123`, retorna: `Produto com código: 123`
