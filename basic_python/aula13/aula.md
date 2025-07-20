# Aula 13 - Operadores Lógicos: `and` e `or`

Esses operadores servem para combinar expressões booleanas (expressões que resultam em `True` ou `False`).

---

## `and`:

Retorna `True` apenas se as duas expressões forem verdadeiras.

```python
print(True and True)        # Saída: True
print(True and False)       # Saída: False
print(False and True)       # Saída: False
print(False and False)      # Saída: False
```

Um exemplo prático pode ser:

```python
age = 25
has_driver_license = True

if age >= 18 and has_driver_license:
    print("Pode dirigir!")
else:
    print("Não pode dirigir")
```

Só imprime "Pode dirigir!" se a pessoa for maior de idade e tiver carteira.

---

## `or`:

Retorna `True` se pelo menos uma das expressões for verdadeira.

```python
print(True and True)        # Saída: True
print(True and False)       # Saída: True
print(False and True)       # Saída: True
print(False and False)      # Saída: False
```
