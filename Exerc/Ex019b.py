import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

nomes = [nome1,nome2,nome3,nome4]
print(nomes)
escolhido = random.randrange(4)
print(nomes[escolhido])
nomes.pop(escolhido)
escolhido = random.randrange(3)
print(nomes[escolhido])
nomes.pop(escolhido)
escolhido = random.randrange(2)
print(nomes[escolhido])
nomes.pop(escolhido)
print(nomes[0])


