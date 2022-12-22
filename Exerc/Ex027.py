nome = input('Digite um nome: ')
nome_dividido = nome.split()
print(nome_dividido[0])
#print(len(nome_dividido))
numero_de_nomes = len(nome_dividido)
if numero_de_nomes >1:
    print(nome_dividido[numero_de_nomes-1])