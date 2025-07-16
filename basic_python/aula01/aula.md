# Aula 01 - Comentários e Docstrings em Python

Comentários são trechos de texto ignorados pelo interpretador.
Eles servem para **explicar o código** para humanos.

## Sintaxe

Use o símbolo `#` para comentar uma linha:

```python
# Este é um comentário
print("Olá") # Comentário ao lado do código
```

> Comentários não são executados

---

## Docstrings

Docstrings (document strings) são strings de documentação usadas para explicar funções, classes ou módulos.
Elas ficam logo após a definição e são escritas entre aspas triplas (`"""` ou `'''`)

```python
def saudacao(nome):
    """
    Retorna uma saudação personalizada.

    Parâmetros:
    nome (str): O nome da pessoa.

    Retorna:
    str: Mensagem de saudação;
    """
    return f"Olá, {nome}!"
```

Você pode acessar essa docstring com:

```python
help(saudacao)
```

---

## Dica

Use comentários para:

-   Explicar trechos complexos.
-   Descrever etapas do código.

Use docstrings para:

-   Documentar o que uma função faz, seus parâmetros e retorno.
