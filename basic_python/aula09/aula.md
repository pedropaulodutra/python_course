# Aula 09 - Formatação de Strings

Existem várias formas de montar mensagens e incluir variáveis dentro de strings em Python.

---

## Usando `f-strings` (forma mais moderna)

Disponível a partir do Python 3.6, é a forma **mais legível e recomendada** hoje em dia.

```python
name = "Pedro"
age = 24
print(f"Meu nome é {name} e tenho {age} anos.")
```

Você pode fazer até expressões dentro da f-string:

```python
age = 24
print(f"Ano que vem terei {age + 1} anos.")
```

---

## Usando o método `.format()`

Forma intermediária, mais antiga que f-strings, mas ainda muito usada.

```python
name = "Pedro"
age = 24
print("Meu nome é {} e tenho {} anos.".format(name, age))
```

Tabém dá pra usar índices ou nomes:

```python
name = "Pedro"
age = 24

print("Meu nome é {0} e tenho {1} anos. {0} gosta de Python".format(name, age))
# ou
print("Meu nome é {n} e tenho {a} anos.".format(n=name, a=age))
```

---

## Usando Interpolação com `%` (forma antiga)

É parecida com a formatação de strings em C.

```python
name = "Pedro"
age = 24
print("Meu nome é %s e tenho %d anos." % (name, age))
```

-   `%s`: string
-   `%d`: inteiro
-   `%f`: float

```python
height = 1.80
print("Minha altura é %.2f metros." % height)
```

---

## Qual usar?

-   Prefira `f-string` (moderna, clara e flexível)
-   `.format()` pode ser útil em situações com muitas variáveis
-   `%` só aparece em códigos antigos, evite em novos projetos
