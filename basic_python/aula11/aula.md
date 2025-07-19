# Aula 11 - Blocos e Condicionais em Python

Blocos são conjuntos de instruções que pertencem a uma mesma estrutura (como uma função, condição ou laço).
Em Python, blocos são definidos por identação (espaço ou tabulação). O padrão é usar 4 espaços.

Exemplo:

```python
age = 18

if age >= 18:
    print("Você é maior de idade")  # Este print está dentro do bloco do if
print("Fim do programa")  # Fora do bloco do if
```

---

## Estruturas condicionais: `if`, `elif`, `else`

Usamos as condições para tomar decisões no código, baseadas em valores e expressões.

`if` (se):

```python
if first_condition:
    # bloso se a condição for verdadeira
```

`elif` (senão se):

```python
if first_condition:
    # bloco se a primeira condição for verdadeira
elif second_condition:
    # bloco se segunda condição for verdadeira
```

`else` (senão):

```python
if first_condition:
    # bloco se a primeira condição for verdadeira
elif second_condition:
    # bloco se segunda condição for verdadeira
else:
    # bloco se nenhuma das duas acimas forem verdadeiras
```

### Exemplo

```python
student_grade = 7

if student_grade >= 7:
    print("Aprovado")
elif student_grade >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

## Dicas

-   Use `:` ao final da linha com `if`, `elif` ou `else`.
-   A indentação é obrigatória em Python. Se errar a indentação, seu código não vai rodar.
-   Expressões podem usar operadores relacionais e lógicos para construir condições
