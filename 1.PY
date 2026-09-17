import os
os.system('cls')

A = int(input('Digite o 1º número: '))
B = int(input('Digite o 2º número: '))
C = int(input('Digite o 3º número: '))

soma= A + B
print(f'Soma: {soma}')

if soma < C:
    print('A soma de A + B é menor que C.')
elif soma > C:
    print('A soma de A + B é maior que C.')
else:
    print('A soma de A + B é igual a C.')