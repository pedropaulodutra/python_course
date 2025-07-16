# Aula 03 - Tipo de dado `str` em Python

-   Em Python, `str` é o tipo de dado usado para representar **textos** (sequências de caracteres).

---

## Criando strings

Strings podem ser criadas com **aspas simples**, **aspas duplas** ou **aspas triplas**:

```python
texto1 = 'Olá'
texto2 = "Mundo"
texto3 = """Texto
com várias
linhas"""
```

---

## Operações com `str`

### Concatenação

```python
nome = "Pedro"
mensagem = "Olá, " + nome
print(mensagem)     # Saída: Olá, Pedro
```

### Repetição

```python
print("ha" * 3)     # Saída: hahaha
```

## Indexação e fatiamento

### Acessar caracteres

```python
texto = "Python"
print(texto[0])     # Saída: P
print(texto[-1])    # Saída: n (última letra)
```

### Fatiar partes das string

```python
texto = "Python"
print(texto[1:4])   # Saída: yth
print(texto[:3])    # Saída: Pyt
```

## Métodos úteis

```python
texto = "   Olá, Mundo!   "
print(texto.lower())    # Saída:    olá, mundo!
print(texto.upper())    # Saída:    OLÁ, MUNDO!
print(texto.strip())    # Saída: Olá, Mundo! (remove espaços nas bordas)
print(texto.replace("Olá", "Oi"))   # Saída:    Oi, mundo!
print(len(texto))       # Saída: 17 (comprimento da string)
```

## Observações

-   Strings são imutáveis: não é possível alterar um caractere direto na string original.
-   Você pode usar f-strings para interpolar variáveis:

```python
nome = "Pedro"
idade = 25
print(f"{nome} tem {idade} anos.")      # Saída: Pedro tem 25 anos.
```

## Verificando tipo

```python
print(type("texto"))        # Saída: <class 'str'>
```

## Caracteres de espace

Usamos o caractere `\` (barra invertida) para inserir símbolos especiáis

| Código       | Significado                        | Exemplo                      | Resultado (visível)        |
| ------------ | ---------------------------------- | ---------------------------- | -------------------------- |
| `\'`         | Aspa simples                       | `'Ele disse: \'Oi\''`        | `Ele disse: 'Oi'`          |
| `\"`         | Aspa dupla                         | `"Ela disse: \"Oi\""`        | `Ela disse: "Oi"`          |
| `\\`         | Barra invertida (`\`)              | `"C:\\Users\\Pedro"`         | `C:\Users\Pedro`           |
| `\n`         | Nova linha (line break)            | `"Linha 1\nLinha 2"`         | Linha 1<br>Linha 2         |
| `\t`         | Tabulação (tab)                    | `"Item:\tValor"`             | `Item:   Valor`            |
| `\r`         | Retorno de carro (carriage return) | `"ABC\rX"`                   | `XBC` (substitui o início) |
| `\b`         | Backspace                          | `"abc\bz"`                   | `abz`                      |
| `\f`         | Form feed (raro)                   | `"Olá\fMundo"`               | `OláMundo`                 |
| `\a`         | Bell (alerta sonoro, se suportado) | `"\a"`                       | _Som ou nada_              |
| `\v`         | Vertical tab (raro)                | `"A\vB"`                     | `AB`                       |
| `\ooo`       | Valor octal                        | `"\141"`                     | `a`                        |
| `\xhh`       | Valor hexadecimal                  | `"\x61"`                     | `a`                        |
| `\N{name}`   | Nome Unicode                       | `"\N{LATIN SMALL LETTER A}"` | `a`                        |
| `\uXXXX`     | Unicode 16 bits                    | `"\u00E1"`                   | `á`                        |
| `\UXXXXXXXX` | Unicode 32 bits                    | `"\U000000E1"`               |

links de apoio:

-   [Métodos de String](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
