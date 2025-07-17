# Aula 06 - Conversão de Tipos (type casting)

Em Python, converter um valor de um tipo para outro é algo comum, e isso é chamado de type casting.

---

## Principais funções de conversão

### `int()`

Converte para número inteiro:

```python
print(int(3.9))      # Saída: 3 (trunca a parte decimal)
print(int("10"))     # Saída: 10
print(int(True))     # Saída: 1
print(int(False))    # Saída: 0
```

### `float()`

Converte para número decimal:

```python
print(float(5))        # Saída: 5.0
print(float("2.5"))    # Saída: 2.5
print(float(True))     # Saída: 1.0
```

### `str()`

Converte qualquer valor para string:

```python
print(str(42))         # Saída: "42"
print(str(3.14))       # Saída: "3.14"
print(str(True))       # Saída: "True"
```

### `bool()`

Converte valores para booleano:

```python
print(bool(0))         # Saída: False
print(bool(42))        # Saída: True
print(bool(""))        # Saída: False
print(bool("texto"))   # Saída: True
```

### Exemplos

```python
idade = "30"
idade_int = int(idade)
print(idade_int + 5)    # Saída: 35
```

```python
preco = 9.99
mensagem = "O produto custa " + str(preco)
print(mensagem)         # Saída: O produto custa 9.99
```

---

## Quando usar conversão de tipos?

-   Para evitar erros em operações entre tipos diferentes
-   Para formatar dados de entrada (ex: `input()` sempre retorna `str`)
-   Para validar e manipular dados corretamente
