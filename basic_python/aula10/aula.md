# Aula 10 - Coletando Dados do Usuário

Em Python, usamos a função `input()` para receber dados digitados pelo usuário.

---

## Sintaxe básica

```python
name = input("Digite seu nome: ")
print(f"Olá, {name}!")
```

-   O que for digitado sempre será retornado como uma string (mesmo que seja um número).

---

## Convertendo tipos

Se quiser trabalhar com números, é necessário converter o valor:

```python
idade = int(input("Digite sua idade: "))
print(type(idade))      # Saída: <class 'int'>
```
