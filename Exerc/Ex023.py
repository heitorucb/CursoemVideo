numero = -1
while numero < 0 or numero >=10000:
    numero = int(input('Digite um número entre 0 e 9999:'))
print('O numero escolhido é: {}'.format(numero))

num_string = str(numero)
quantidade_de_caracteres = len(num_string)
#print(quantidade_de_caracteres)
if quantidade_de_caracteres == 4:
    print('Unidade: {}'.format(num_string[3]))
    print('Dezendas: {}'.format(num_string[2]))
    print('Centenas: {}'.format(num_string[1]))
    print('Milhares: {}'.format(num_string[0]))
if quantidade_de_caracteres == 3:
    print('Unidade: {}'.format(num_string[2]))
    print('Dezendas: {}'.format(num_string[1]))
    print('Centenas: {}'.format(num_string[0]))
    print('Milhares: {}'.format(0))
if quantidade_de_caracteres == 2:
    print('Unidade: {}'.format(num_string[1]))
    print('Dezendas: {}'.format(num_string[0]))
    print('Centenas: {}'.format(0))
    print('Milhares: {}'.format(0))
if quantidade_de_caracteres == 1:
    print('Unidade: {}'.format(num_string[0]))
    print('Dezendas: {}'.format(0))
    print('Centenas: {}'.format(0))
    print('Milhares: {}'.format(0))