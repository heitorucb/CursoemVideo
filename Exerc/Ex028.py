import random
lista = [0,1,2,3,4,5]
escolha_computador = random.choice(lista)
escolha_pessoa = int(input('Escolha um número entre 0 e 5: '))

if escolha_pessoa == escolha_computador:
    print('Você acertou')
else:
    print('Você perdeu')
    print('O número escolhido foi: {}'.format(escolha_computador))
