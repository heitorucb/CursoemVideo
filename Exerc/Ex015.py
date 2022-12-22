dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Qual a quilometragem percorrida? '))
print('O valor a pagar é {:.2f}'.format(dias*60+km*0.15))
