import sys
import os
import importlib
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch

# Adiciona a raiz do repositório ao path para importar os módulos exercicio*.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

class Autograder:
    
    @staticmethod
    def main(args):
        if len(args) == 0:
            Autograder.fail("Modo nao informado. Use: ex1 | ex2 | ex3 | ex4 | ex5 | ex6")
        
        try:
            mode = args[0].strip().lower()
            if mode == "ex1":
                Autograder.test_ex1()
            elif mode == "ex2":
                Autograder.test_ex2()
            elif mode == "ex3":
                Autograder.test_ex3()
            elif mode == "ex4":
                Autograder.test_ex4()
            elif mode == "ex5":
                Autograder.test_ex5()
            elif mode == "ex6":
                Autograder.test_ex6()
            else:
                Autograder.fail(f"Modo invalido: {mode}")
            
            Autograder.pass_test()
        
        except AssertionError as e:
            Autograder.fail(str(e))
        except Exception as e:
            cause = str(e.__cause__) if e.__cause__ else "sem causa"
            Autograder.fail(f"Erro ao executar avaliacao: {str(e)} | Causa: {cause}")
    
    @staticmethod
    def test_ex1():
        output1 = Autograder.capture_output("exercicio1", "Exercicio1", "verificar_paridade", "8")
        Autograder.assert_true("par" in output1.lower(), "Deve identificar numero par")

        output2 = Autograder.capture_output("exercicio1", "Exercicio1", "verificar_paridade", "7")
        Autograder.assert_true("impar" in output2.lower(), "Deve identificar numero impar")
    
    @staticmethod
    def test_ex2():
        output1 = Autograder.capture_output("exercicio2", "Exercicio2", "verificar_sinal", "10")
        Autograder.assert_true("positivo" in output1.lower(), "Deve identificar numero positivo")

        output2 = Autograder.capture_output("exercicio2", "Exercicio2", "verificar_sinal", "-3")
        Autograder.assert_true("negativo" in output2.lower(), "Deve identificar numero negativo")

        output3 = Autograder.capture_output("exercicio2", "Exercicio2", "verificar_sinal", "0")
        Autograder.assert_true("zero" in output3.lower(), "Deve identificar zero")
    
    @staticmethod
    def test_ex3():
        output1 = Autograder.capture_output("exercicio3", "Exercicio3", "validar_horario", "23\n59")
        Autograder.assert_true("valido" in output1.lower(), "Deve aceitar horario dentro do intervalo")

        output2 = Autograder.capture_output("exercicio3", "Exercicio3", "validar_horario", "24\n10")
        Autograder.assert_true("invalido" in output2.lower(), "Deve rejeitar hora fora do intervalo")

        output3 = Autograder.capture_output("exercicio3", "Exercicio3", "validar_horario", "12\n60")
        Autograder.assert_true("invalido" in output3.lower(), "Deve rejeitar minuto fora do intervalo")
    
    @staticmethod
    def test_ex4():
        output1 = Autograder.capture_output("exercicio4", "Exercicio4", "exibir_maior", "10\n5")
        Autograder.assert_true("10" in output1, "Deve exibir o maior valor")

        output2 = Autograder.capture_output("exercicio4", "Exercicio4", "exibir_maior", "7\n7")
        Autograder.assert_true("numeros iguais" in output2.lower(), "Deve informar quando os valores sao iguais")
    
    @staticmethod
    def test_ex5():
        output1 = Autograder.capture_output("exercicio5", "Exercicio5", "exibir_menor", "9\n3\n5")
        Autograder.assert_true("3" in output1, "Deve exibir o menor valor")

        output2 = Autograder.capture_output("exercicio5", "Exercicio5", "exibir_menor", "4\n4\n4")
        Autograder.assert_true("numeros iguais" in output2.lower(), "Deve informar quando todos os valores sao iguais")
    
    @staticmethod
    def test_ex6():
        output1 = Autograder.capture_output("exercicio6", "Exercicio6", "calcular_salario_total", "2000\n4000")
        Autograder.assert_true("comissao: r$ 200.00" in output1.lower(), "Deve calcular 5% de comissao ate R$ 5.000,00")
        Autograder.assert_true("salario total: r$ 2200.00" in output1.lower(), "Deve somar salario fixo e comissao")

        output2 = Autograder.capture_output("exercicio6", "Exercicio6", "calcular_salario_total", "2000\n7000")
        Autograder.assert_true("comissao: r$ 390.00" in output2.lower(), "Deve aplicar 7% sobre vendas acima de R$ 5.000,00")
        Autograder.assert_true("salario total: r$ 2390.00" in output2.lower(), "Deve exibir salario total correto")
    
    @staticmethod
    def capture_output(module_name, class_name, method_name, input_data):
        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            instance = cls()
            method = getattr(instance, method_name)
            
            # Capturar saída e simular entrada
            output_buffer = StringIO()
            input_lines = input_data.strip().split('\n')
            
            with redirect_stdout(output_buffer):
                with patch('builtins.input', side_effect=input_lines):
                    method()
            
            return output_buffer.getvalue()
        
        except Exception as e:
            cause = str(e.__cause__) if e.__cause__ else "sem causa"
            raise Exception(f"Erro ao executar {class_name}.{method_name}: {str(e)} | Causa: {cause}")
    
    @staticmethod
    def assert_true(condition, message):
        if not condition:
            raise AssertionError(message)
    
    @staticmethod
    def pass_test():
        print("OK!")
    
    @staticmethod
    def fail(message):
        print(f"FAIL: {message}")
        sys.exit(1)

if __name__ == "__main__":
    Autograder.main(sys.argv[1:])