import os
os.system('cls')

A = int(input('Digite o 1º número: '))
B = int(input('Digite o 2º número: '))

soma = A + B
multiplicacao = A * B
if A == B:
    resultado = soma
    print(f'Resultado: {soma}')
else:
    resultado = multiplicacao
    print(f'Resultado: {multiplicacao}')
