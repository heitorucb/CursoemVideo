numero = -1
while numero < 0 or numero >=10000:
    numero = int(input('Digite um número entre 0 e 9999:'))
print('O numero escolhido é: {}'.format(numero))

print('Unidade: {}'.format(numero % 10))
print('Dezena: {}'.format(numero //10 % 10))
print('Centena: {}'.format(numero //100 % 10))
print('Milhar: {}'.format(numero //1000 % 10))