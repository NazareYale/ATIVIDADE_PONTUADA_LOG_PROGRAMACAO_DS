import os
os.system('cls')


tipo = input("Tipo de combustivel (A-alcool, G-gasolina): ").upper()
litros = float(input("Quantidade de litros vendidos: "))

if tipo == "A":
    preco = 3.79
    if litros <= 25:
        desconto = 0.10
    else:
        desconto = 0.20
elif tipo == "G":
    preco = 6.59
    if litros <= 25:
        desconto = 0.15
    else:
        desconto = 0.30
else:
    preco = 0
    desconto = 0
    print("Tipo de combustivel invalido.")

if tipo in ("A", "G"):
    valor_bruto = litros * preco
    valor_final = valor_bruto * (1 - desconto)
    print(f"Valor a pagar: R$ {valor_final:.2f}")
