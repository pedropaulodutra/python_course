# Aula 05 - Tipo Booleano em Python: `bool`

O tipo `bool` representa **valores lógicos**, usados para decisões e comparações.

---

## `bool`

O tipo `bool` possui apenas **dois valores** possíveis:

-   `True` → verdadeiro
-   `False` → falso

> A primeira letra **deve ser maiúscula** (`true` e `false` com minúscula causam erro).

### Exemplos:

```python
ativo = True
pago = False
```

---

## Verificando tipo

```python
print(type(True))       # Saída: <class 'bool'>
print(type(False))       # Saída: <class 'bool'>
```

---

## Comparações que retornam `bool`

```python
print(10 > 5)        # Saída: True
print(3 == 3)        # Saída: True
print("oi" != "tchau")  # Saída: True
print(7 < 2)         # Saída: False
```

---

## Conversão para booleano com `bool()`

Alguns valores retornam `False` quando convertidos para booleanos, são eles:

-   0
-   0.0
-   '' (string vazia)
-   [] (lista vazia)
-   None

Qualquer outro valor é convertido como `True`

### Exemplos

```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("abc"))    # True
print(bool([]))       # False
```

---

## Operadores lógicos

-   `and`: retorna `True` se ambos os lados forem verdadeiros
-   `or`: retorna `True` se pelo menos um for verdadeiro
-   `not`: inverte o valor lógico

### Exemplos

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```
