import os
os.system('cls')

operacao = input("Digite a operacao (+, -, *, /): ")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if operacao == "+":
    print(f"{a} + {b} = {a + b}")
elif operacao == "-":
    print(f"{a} - {b} = {a - b}")
elif operacao == "*":
    print(f"{a} * {b} = {a * b}")
elif operacao == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Erro: divisao por zero.")
else:
    print("Operacao invalida.")
