# Aula 08 - Operadores Matemáticos

Python permite fazer operações matemáticas básicas com facilidade usando operadores.

---

## Operadores Aritméticos

| Operador                  | Símbolo | Exemplo   | Resultado     |
| ------------------------- | ------- | --------- | ------------- |
| Adição                    | `+`     | `10 + 5`  | `15`          |
| Subtração                 | `-`     | `10 - 5`  | `5`           |
| Multiplicação             | `*`     | `10 * 5`  | `50`          |
| Divisão                   | `/`     | `10 / 5`  | `2.0` (float) |
| Divisão inteira           | `//`    | `10 // 3` | `3`           |
| Resto da divisão (módulo) | `%`     | `10 % 3`  | `1`           |
| Potência                  | `**`    | `2 ** 3`  | `8`           |

---

## Exemplos práticos

```python
a = 10
b = 3

print(a + b)   # Saída: 13
print(a - b)   # Saída: 7
print(a * b)   # Saída: 30
print(a / b)   # Saída: 3.333...
print(a // b)  # Saída: 3
print(a % b)   # Saída: 1
print(a ** b)  # Saída: 1000
```

---

## Observações

-   A divisão com `/` sempre retorna um número `float`
-   A divisão com `//` ignora as casas decimais e retorna um `int` (se ambos os operandos forem `int`)
-   O operador `%` é muito usado para descobrir se um número é par ou ímpar

---

## Operadores com Strings

Em Python, alguns operadores também funcionam com **strings**, o que facilita muito a manipulação de textos.

### Concatenação (`+`)

Usado para juntar duas ou mais strings

```python
name = "Pedro"
surname = "Dutra"
print(name + " " + surname)     # Saída: Pedro Dutra
```

### Repetição

Usado para repetir a string o número de vezes especificado

```python
print("ha" * 3)     # Saída: hahaha
```

---

## Precedência entre os operadores aritméticos

Em expressões com múltiplos operadores, o Python segue uma **ordem de precedência**, ou seja, a ordem em que as operações são resolvidas.

A ordem é parecida com a da matemática:

| Ordem | Operador            | Descrição                                       |
| ----- | ------------------- | ----------------------------------------------- |
| 1     | `()`                | Parênteses                                      |
| 2     | `**`                | Exponenciação                                   |
| 3     | `*`, `/`, `//`, `%` | Multiplicação, divisão, divisão inteira, módulo |
| 4     | `+`, `-`            | Soma e subtração                                |

### Exemplos

```python
result = 2 + 3 * 4
print(result)       # Saída: 14 (porque a multiplicação vem antes da soma)
```

Se quiser forçar uma ordem diferente, use parênteses:

```python
result = (2 + 3) * 4
print(result)       # Saída: 20
```
