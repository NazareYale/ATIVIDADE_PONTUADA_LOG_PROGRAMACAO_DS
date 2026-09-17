import os
os.system('cls')

qtd_morango = float(input("Quantidade de morango (Kg): "))
qtd_maca = float(input("Quantidade de maca (Kg): "))

if qtd_morango <= 5:
    valor_morango = qtd_morango * 2.50
else:
    valor_morango = qtd_morango * 2.20

if qtd_maca <= 5:
    valor_maca = qtd_maca * 1.80
else:
    valor_maca = qtd_maca * 1.50

total = valor_morango + valor_maca
total_kg = qtd_morango + qtd_maca

if total_kg >= 10 or total > 15:
    total = total * 0.9

print(f"Valor a pagar: R$ {total:.2f}")

    
