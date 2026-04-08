#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/grade_python.py <ex1|ex2|ex3|ex4|ex5|ex6>")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    print(f"🧪 Executando teste Python para {mode}...")
    
    try:
  
        result = subprocess.run([sys.executable, "autograder.py", mode], 
                              capture_output=True, text=True, check=True, 
                              cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        print(result.stdout)
        print("Teste concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"ERRO: {e.stderr}")
        print(f"Saída: {e.stdout}")
        sys.exit(1)

if __name__ == "__main__":
    main()