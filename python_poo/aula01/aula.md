# Aula 01 - O que são classes

Classes são **modelos (ou moldes)** para criar objetos com **atributos** e **métodos (funções)**.

Se você pense em **orientação a objetos**, a classe é como o "projeto", e os **objetos** são as "coisas construídas com esse projeto".

---

## Exemplo da vida real

Imagine uma **classe** chamada `Casa`.  
Ela pode ter:

-   **Atributos**: cor, número de quartos, metragem
-   **Métodos**: abrir_porta(), acender_luz()

Com isso, você pode criar **várias casas diferentes**, cada uma com suas características.

---

## Sintaxe

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome    # atributo
        self.idade = idade  # atributo

    def apresentar(self):   # método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Pedro", 24)
p2 = Pessoa("Kathleen", 23)

p1.apresentar()     # Saída: Olá, meu nome é Pedro e tenho 24 anos.
p2.apresentar()     # Saída: Olá, meu nome é Kathleen e tenho 23 anos.
```

---

## Atributos vs Métodos

Em programação orientada a objetos (POO), nossas **classes** podem ter **atributos** e **métodos**

### O que são atributos?

Atributos são **variáveis que pertencem ao objeto**.
Eles armazenam **informações** sobre o estado do objeto

por exemplo:

```python
class Fogao:
    def __init__(self, num_bocas, gas_ligado):
        self.num_bocas = num_bocas      # atributo
        self.gas_ligado = gas_ligado    # atributo

    def ligar_boca(self, boca):   # método
        if boca > self.num_bocas:
            return f"Fogão tem menos bocas"
        if not gas_ligado:
            return f"Gás desligado"
        return f"Boca {boca} do fogão acesa"
```

como pode verificar, o objeto Fogao tem atributos que contém informações sobre o estado, como quantidade de bocas no fogao, se o fogao tem gás para trabalhar

### O que são métodos?

Métodos são funções dentro de uma classe, usadas para realizar ações com os atributos do objeto, no exemplo acima temos um método chamado `ligar_boca` que dependendo do estado dos atributos ele pode ou não ligar a boca de um fogão.

---

## O que é `__init__` em Python?

O método `__init__` é um **método especial** usado para **inicializar objetos** criados a partir de uma classe.  
Ele é chamado **automaticamente** sempre que você cria um novo objeto.

Serve para:

-   Definir os **atributos iniciais** do objeto
-   Passar **valores personalizados** na hora da criação
-   Preparar o objeto para uso

### Sintaxe

```python
class NomeDaClasse:
    def __init__(self, parametros):
        self.atributo = valor
```

O primeiro parâmetro sempre é self, que representa o próprio objeto sendo criado

### Explicando o `self`

-   `self` é uma referência ao próprio objeto
-   Permite acessar ou definir atributos e métodos da instância

### Observações

Você não chama `__init__` diretamente. Ele é executado automaticamente quando você inicializa um objeto.

---

## Boas práticas

-   Use o `__init__` para configurar os atributos da instância.
-   Crie métodos com nomes descritivos e em letras minúsculas com underline [snake_case](https://www.theserverside.com/definition/Snake-case)
-   Evite nomes muito genéricos (`Data`, `Info`, `Object`) que não dizem nada sobre o propósito da classe.
-   Nomes de classes devem começar com letra maíuscula seguindo o padrão [PascalCase](https://www.theserverside.com/definition/Pascal-case)

### Mas por que `int`, `str`, `list` começam com letra minúscula?

As classes built-in (`int`, `str`, `list`, etc.) usam nomes minúsculos por questões históricas e de simplicidade:

-   Essas classes foram pensadas para parecerem tipos primitivos, mesmo sendo objetos reais.
-   Python foi feito para parecer simples, e `int(x)` se parece com `int` como tipo, como se fosse uma palavra-chave — mesmo sendo uma classe por trás.
