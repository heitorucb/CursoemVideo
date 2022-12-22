n = (input('Digite algo, por favor: '))
n = n.split()
print(n)
print("\n")

for i in n:
    if i.isupper():
        print(f'{i} está em CAIXA ALTA')
    else:
        print('{} Não está em CAIXA ALTA.'.format(i))




