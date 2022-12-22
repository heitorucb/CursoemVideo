numero = int(input('Digite um valor: '))
print('Qual será a base para conversão\n1-para binário\n2-para octal\n3-hexadecimal')
opcao = int(input())
if opcao == 1:
    print('{}'.format(bin(numero)[2:]))
elif opcao == 2:
    print('{}'.format(oct(numero)[2:]))
elif opcao == 3:
    print('{}'.format(hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
