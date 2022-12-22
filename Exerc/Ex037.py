numero = int(input('Digite um valor: '))
print('Qual será a base para conversão\n1-para binário\n2-para octal\n3-hexadecimal')
opcao = int(input())
if opcao == 1:
    print('{:#b}'.format(numero))
elif opcao == 2:
    print('{:08b}'.format(numero))
else:
    print('{:16b}'.format(numero))