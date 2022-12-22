lista = []
for i in range(3):
    lista.append(int(input('Digite o comprimento da reta {}: '.format(i+1))))
print(lista)
ordenanda = sorted(lista)
print(ordenanda)
if ordenanda[2] < ordenanda[0]+ordenanda[1]:
    print('É possível formar um triângulo')
    if ordenanda.count(ordenanda[0]) == 3:
        print('Este triangulo é Equilátero.')
    elif ordenanda.count(ordenanda[0]) == 2 or ordenanda.count(ordenanda[1]) == 2:
        print('Este triângulo é Isóceles.')
    else:
        print('Este triangulo é Escaleno.')
else:
    print('Não é possível formar um triângulo')

