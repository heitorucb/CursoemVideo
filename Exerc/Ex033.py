lista = []
for i in range(5):
 num = int(input('digite um número: '))
 lista.append(num)
print('O maior número é: {}'.format(max(lista)))
print('O menor número é: {}'.format(min(lista)))