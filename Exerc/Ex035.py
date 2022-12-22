lista = []
for i in range(3):
    lista.append(int(input('Digite o comprimento da reta {}: '.format(i+1))))
print(lista)
ordenanda = sorted(lista)
print(ordenanda)
if ordenanda[2] < ordenanda[0]+ordenanda[1]:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')


