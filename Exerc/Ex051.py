primeiro_termo = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
n = primeiro_termo
lista = []
lista.append(primeiro_termo)
print(primeiro_termo)
for i in range(9):
    n += razao
    lista.append(n)
    print(n)
print(lista)
