import os
os.system('cls')

notaA = float(input('Digite a sua 1º nota: '))
notaB = float(input('Digite a sua 2º nota: '))

media = (notaA + notaB) / 2

if media >= 6:
    print('APROVADO!')
elif media >4:
    print('EM RECUPERAÇÃO.')
else:
    print('REPROVADO.')
