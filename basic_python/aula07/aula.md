# Aula 07 - Variáveis

Variáveis são **espaços na memória** que armazenam informações para que possamos usá-las depois.  
Em Python, você **não precisa declarar o tipo da variável**. O próprio Python entende qual é o tipo com base no valor que você atribui por conta da tipagem dinâmica.

## Como criar variáveis?

```python
nome = "Pedro"
idade = 25
altura = 1.75
```

---

## O que posso colocar nas variáveis?

Todos os tipos de dados que vimos anteriormente, `str`, `int`, `float`, `bool`

---

## Regras para nomear variáveis

De acordo com a PEP8, variáveis:

-   Devem manter o padrão `snake_case` utilizando letras minúsculas e `_` para separar
-   Devem usar nomes descritivos e em inglês, como `name`, `product_price`
-   Se for variável booleana, indique isso no nome (ex: `is_active = True`, `has_access = False`, `is_logged_in = True`)

Exemplos:

```python
user_name = "Pedro"
product_price = 19.90
is_admin = True
```

---

## Dica

Você pode trocar o valor de uma variável a qualquer momento:

```python
x = 5
x = "Agora sou um texto"
```
