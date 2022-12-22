nome = input('Qual é seu nome: ')
if nome == 'Heitor':
    print('Seu nome é bem bonito!')
elif nome == 'João' or nome =='Maria' or nome =='José':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Heitor MACHADO Franco Albernaz Farofa Carlinhos':
    print('Seu nome é ótimo!')
    print(nome in 'Heitor MACHADO Franco Albernaz Farofa Carlinhos')
else:
    print('Tenha um bom dia!')

