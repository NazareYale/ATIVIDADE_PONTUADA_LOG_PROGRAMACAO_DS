import os
os.system('cls')

macas = float(input('Digite quantos kilos de maçãs vai ser comprado: '))
morango = float(input('Digite quantos kilos de morango vai ser comprado: '))
valores =  valor = macas * 1.80 | valor2 = macas * 1.50 | valor3 = morango * 2.50 | valor4 = morango * 2.20

if macas and morango > 10 or valores > 15:
    resultado = valores * 0.10
elif macas and morango <= 5:
    print(valor and valor3)
elif macas and morango >5:
    print(valor2 and valor4)

    
