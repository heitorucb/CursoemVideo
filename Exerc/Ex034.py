salario = float(input('Digite seu saário: '))
if salario > 1250:
    print('Seu salário teve um aumento de 10% e agora passou para R${:.2f}'.format(salario*1.1))
else:
    print('Seu salário teve um aumento de 15% e agora passou para R${:.2f}'.format(salario*1.15))