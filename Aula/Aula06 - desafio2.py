n = 'x'
print(type(n))
while n.isspace() != True:
    n = input('Digite qualquer coisa: ')
    print(type(n))
    if n.isupper():
        print('É todo em caixa alta.')
    elif n.isnumeric():
        print('É um número.')
    elif n.isalpha():
        print('É uma letra.')
    elif n.isalnum():
        print('É alfa-numérico')
    else:
        print('Não consegui identificar seu tipo')
print('É um espaço. O programa será fechado')
