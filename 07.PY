import os
os.system('cls')

produto = str(input('Digite o nome do produto: '))
quant_produto = float(input('Digite a quantidade adquirida: '))
preco_unitario = float(input('Digite o preço unitário: '))


total = quant_produto * preco_unitario


if quant_produto <= 5:
    desconto = total *  0.02
elif quant_produto <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_a_pagar = total - desconto

print(f'Produto: {produto}')
print(f'Quantidade: {quant_produto}')
print(f'Preço unitário: {preco_unitario}')
print(f'Total a pagar: {total_a_pagar}')
