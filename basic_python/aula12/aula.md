# Aula 12 - Operadores de Comparação

Os operadores de comparação são usados para comparar valores e retornam um resultado booleano:
`True` (verdadeiro) ou `False` (falso).

> Dica: eles se dão muito bem com as condicionais vistas na aula anterior

---

## Operadores disponíveis:

| Operador | Significado      | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `==`     | Igual a          | `5 == 5` | `True`    |
| `!=`     | Diferente de     | `4 != 3` | `True`    |
| `>`      | Maior que        | `7 > 2`  | `True`    |
| `<`      | Menor que        | `1 < 3`  | `True`    |
| `>=`     | Maior ou igual a | `8 >= 8` | `True`    |
| `<=`     | Menor ou igual a | `6 <= 5` | `False`   |

### Exemplos

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(a <= 10)  # True
print(b >= 15)  # True
```

---

## Condicionais com comparação

Nossos operadores condicionais executam apenas valores truthy, e os operadores de comparação retornam sempre um valor booleano (True ou False). Isso permite que você utilize comparações diretamente dentro de estruturas condicionais.

Por exemplo, vamos imaginar um código que calcula a idade de uma pessoa com base no ano de nascimento. Se a idade for maior ou igual a 18, consideramos a pessoa adulta. Caso contrário, ela ainda é menor de idade.

```python
birth_year = 2001
actual_year = 2025
age = actual_year - birth_year

if age >= 18:
    print("Adulto")
else:
    print("Menor de idade")
```

---

## Observações

-   O operador `=` não é de comparação, é de atribuição.
-   Use sempre `==` quando quiser verificar igualdade.
-   Esses operadores são muito usados dentro de estruturtas como o `if`.
