import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome')

lista = [n1, n2, n3, n4]
print(lista)
random.shuffle(lista)
print(lista)