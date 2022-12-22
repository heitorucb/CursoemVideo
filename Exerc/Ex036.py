casa = float(input('Digite o valor da casa:\n'))
salario = float(input('Digite o valor do salário:\n'))
anos = int(input('Quantos anos irá pagar esta casa:\n'))

prestacao = casa/(anos * 12)
salario_aval = salario * 0.3

print('O valor da casa é de R${:.2f}\nA casa será paga em {} meses\nA prestação ficará em R${:.2f}\n30% do seu salário é R${:.2f}'.format(casa,anos*12,prestacao,salario_aval))

if salario_aval > prestacao:
    print('A casa foi aprovada!')
else:
    print('A casa não foi aprovada')

