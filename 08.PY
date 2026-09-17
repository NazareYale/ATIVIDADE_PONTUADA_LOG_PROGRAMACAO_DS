import os
os.system('cls')

Cd = str(input('Digite a qual a cor do seu CD: '))

match Cd:

    case 'verde':
        print('R$ 10')
    case 'azul':
        print('R$ 20')
    case 'amarelo':
        print('R$ 30')
    case 'vermelho':
        print('R$ 40')
