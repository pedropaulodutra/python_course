# Aula 04 - Tipos numéricos em Python: `int` e `float`

Em Python, usamos os tipos `int` e `float` para trabalhar com **números**.

---

## `int`

Representa **números inteiros**, positivos ou negativos, sem parte decimal.

### Exemplos:

```python
idade = 25
saldo = -100
populacao = 200000
```

## `float`

Representa **números de ponto flutuante (decimais)**, também positivos ou negativos.

### Exemplos:

```python
altura = 1.75
temperatura = -4.3
pi = 3.14159
```

---

## Verificando tipos

```python
print(type(42))     # Saída: <class 'int'>
print(type(3.14))     # Saída: <class 'float'>
```

---

## Conversão entre tipos

### `int()` para converter para inteiro

(Trunca a parte decimal)

```python
print(int(3.9))     # Saída: 3
print(int("10"))    # Saída: 10
```

### `float()` para converter para decimal

```python
print(float(5))     # Saída: 5.0
print(float("2.5")) # Saída: 2.5
```

---

## Operações básicas

-   `+`: Adição
-   `-`: Subtração
-   `*`: Multiplicação
-   `/`: Divisão (retorna float)
-   `//`: Divisão inteira (não retorna float)
-   `%`: Módulo (resto da divisão)
-   `**`: Potência

---

## Observações

-   Toda divisão com `/` retorna `float`, mesmo que o resultado seja exato:

```python
print(10 / 2)       # Saída: 5.0
```

-   `float` pode causar imprecisões por causa do jeito que números decimais são armazenados na memória:

```python
print(0.1 + 0.2)    # Saída: 0.3000000000004
```

links de apoio:

-   [Tipos numéricos](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
