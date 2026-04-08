from exercicio1 import Exercicio1
from exercicio2 import Exercicio2
from exercicio3 import Exercicio3
from exercicio4 import Exercicio4
from exercicio5 import Exercicio5
from exercicio6 import Exercicio6

def main():
  

    print("\n--- Exercicio 1: Numero Par ou Impar ---")
    ex1 = Exercicio1()
    ex1.verificar_paridade()

    print("\n--- Exercicio 2: Numero Positivo, Negativo ou Zero ---")
    ex2 = Exercicio2()
    ex2.verificar_sinal()

    print("\n--- Exercicio 3: Validacao de Horario ---")
    ex3 = Exercicio3()
    ex3.validar_horario()

    print("\n--- Exercicio 4: Maior entre Dois Valores ---")
    ex4 = Exercicio4()
    ex4.exibir_maior()

    print("\n--- Exercicio 5: Menor entre Tres Valores ---")
    ex5 = Exercicio5()
    ex5.exibir_menor()

    print("\n--- Exercicio 6: Salario de Vendedor ---")
    ex6 = Exercicio6()
    ex6.calcular_salario_total()

if __name__ == "__main__":
    main()