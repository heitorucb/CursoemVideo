cidade = input('Digite o nome da uma cidade: ')
prime_nome = cidade.split()
primeiro_nome = prime_nome[0].capitalize()
if primeiro_nome == 'Santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
