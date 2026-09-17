import os
os.system('cls')

nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: ')
estado_civil = input('Digite o seu estado civil: ')

if sexo == 'F' and estado_civil == 'CASADA':
    casada = input('Digite seus anos de casada: ')
    print(f'nome: {nome}')
    print(f'Sexo: {sexo}')
    print(f'Estado Civil: {estado_civil}')
    print(f'Anos de Casada: {casada}')
elif estado_civil == 'SOLTEIRO' or 'SOLTEIRA':
    print(f'nome: {nome}')
    print(f'Sexo: {sexo}')
    print(f'Estado Civil: {estado_civil}')
else:
    print('Inválido!')
