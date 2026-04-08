#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: python grade.py <ex1|ex2|ex3|ex4|ex5|ex6>")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    print("🧪 Executando teste para", mode, "...")
    
    try:
        # Executar o autograder
        autograder_path = os.path.join(os.path.dirname(__file__), "autograder.py")
        result = subprocess.run([sys.executable, autograder_path, mode], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        print("Teste concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"ERRO: {e.stderr}")
        print(f"Saída: {e.stdout}")
        sys.exit(1)

if __name__ == "__main__":
    main()