lista = []
for i in range(1,7):
    x = int(input(f'{i} - Digite um valor: '))
    if x % 2 == 0:
        lista.append(x)
print(sum(lista))

