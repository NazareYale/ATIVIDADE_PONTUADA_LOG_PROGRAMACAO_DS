import os
os.system('cls')

renda = float(input('Digite sua renda mensal: R$ '))
emprestimo = float(input('Digite o valor do seu empréstimo: R$ '))
prestacoes = int(input('Digite a quantidade de prestações: '))

prestacao = emprestimo  / prestacoes
maior_emprestimo = renda * 10
maior_prestacao = renda * 0.3

if emprestimo <= maior_emprestimo and prestacao <= maior_prestacao:
    print('Emprestimo aprovado')
else:
    print('Emprestimo reprovado')
