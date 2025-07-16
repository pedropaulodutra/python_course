# Aula 02 - print()

A função `print()` é usada para **exibir informações no terminal**. Ela pode mostrar textos, números, variáveis ou o resultado de expressõe.

---

## Sintaxe

```python
print(valor1, valor2, ..., sep=' ', end='\n')
```

-   `valor1`, `valor2`, `...`: o que será exibido.
-   `sep`: separador entre os valores (padrão é o espaço `' '`).
-   `end`: o que é colocado no final (padrão é `\n`, que quebra a linha).

---

## Exemplos

```python
print("Olá, mundo!")            # Exibe um texto
print(10 + 5)                   # Exibe o resultado de uma operação
nome = "Pedro"
print("Seu nome é", nome)       # Exibe texto com variável
print("a", "b", "c", sep="-")   # Saída: a-b-c
print("Fim", end="!")           # Saída: Fim!
```

---

## Observações

-   `print()` sempre insere uma quebra de linha ao final, a menos que o argumento `end` seja alterado.
-   É uma das funções mais usadas para depuração (debug) e exibição de dados em programas Python
