# Lista 3 - Computational Thinking Using Python

## Sumario
- [Descricao](#descricao)
- [Como utilizar](#como-utilizar)
- [Avaliacao automatica](#avaliacao-automatica)
- [Enunciado dos exercicios](#enunciado-dos-exercicios)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Requisitos de implementacao](#requisitos-de-implementacao)

## Descricao
Este projeto contem 6 exercicios em Python com foco em:

- Entrada de dados com `input()`
- Saida de dados com `print()`
- Estruturas condicionais

## Como utilizar
Implemente cada exercicio no arquivo correspondente e use os comandos abaixo para executar ou validar.

```bash
python app.py
python autograder.py ex1
python grade.py ex1
```

Modos validos: `ex1`, `ex2`, `ex3`, `ex4`, `ex5`, `ex6`.

## Avaliacao automatica
O autograder simula entradas e valida as saidas dos metodos:

- `Exercicio1.verificar_paridade()`
- `Exercicio2.verificar_sinal()`
- `Exercicio3.validar_horario()`
- `Exercicio4.exibir_maior()`
- `Exercicio5.exibir_menor()`
- `Exercicio6.calcular_salario_total()`

## Enunciado dos exercicios

### Exercicio 1
Solicite um valor inteiro e exiba a mensagem `E numero par` ou `E numero impar`.

### Exercicio 2
Solicite um valor inteiro e exiba a mensagem `E positivo`, `E negativo` ou `E zero`.

### Exercicio 3
Solicite dois valores inteiros, um para horas e outro para minutos. Valide se horas esta entre 0 e 23 e se minutos esta entre 0 e 59.

### Exercicio 4
Solicite dois valores inteiros e exiba apenas o maior. Caso sejam iguais, exiba `Numeros iguais`.

### Exercicio 5
Solicite tres valores inteiros e exiba apenas o menor. Caso todos sejam iguais, exiba `Numeros iguais`.

### Exercicio 6
Calcule o salario de um vendedor solicitando:

- Salario fixo
- Valor de vendas

Calcule 5% de comissao sobre vendas de ate R$ 5.000,00 e 7% sobre o valor que ultrapassar esse limite. Exiba a comissao e o salario total.

## Estrutura do projeto

```text
.
├── README.md
├── app.py
├── autograder.py
├── grade.py
├── exercicio1.py
├── exercicio2.py
├── exercicio3.py
├── exercicio4.py
├── exercicio5.py
└── exercicio6.py
```

## Requisitos de implementacao
- Use Python 3.6 ou superior
- Mantenha a estrutura de classes
- Use `input()` para entrada de dados
- Use `print()` para saida de dados
- Mantenha os nomes dos metodos esperados pelo autograder
