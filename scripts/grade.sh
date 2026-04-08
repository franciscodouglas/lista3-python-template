#!/bin/bash

# Script de avaliação para exercícios Python
# Este script chama o autograder Python

if [ $# -eq 0 ]; then
    echo "Uso: bash scripts/grade.sh <ex1|ex2|ex3|ex4|ex5|ex6>"
    exit 1
fi

MODE=$1

echo "🧪 Executando teste para $MODE..."

# Executar o autograder Python
python3 autograder.py $MODE

exit $?