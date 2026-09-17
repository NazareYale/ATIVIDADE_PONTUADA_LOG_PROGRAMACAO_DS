import os
os.system('cls')


litros = float(input('Digite a quantidade de litros vendidos: '))
combustivel = str(input('Digite o seu tipo de combustível(A/G): '))

gasolina = 6.59
alcool = 3.79

if alcool <= 25:
    desconto = alcool - 0.10
elif alcool > 25:
    desconto = alcool - 0.20
elif gasolina <= 25:
    desconto = gasolina - 0.15
else:
    desconto = gasolina - 0.30

print(litros)
print(combustivel)
print(alcool)
print(gasolina)