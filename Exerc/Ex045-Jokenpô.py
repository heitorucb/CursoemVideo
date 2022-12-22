from random import choice
lista = [1,2,3]
pontos_humano = 0
pontos_computador = 0
empate = 0
for i in range(5):
    computador = choice(lista)
    print('-' * 15, 'Rodada número: ',i+1 ,'-'*15)
    humano = 4
    while humano > 3:
        humano = int(input('Digite:\n'
                           '1 para pedra\n'
                           '2 para papel\n'
                           '3 para tesoura\n'))
    if computador == 1:
        print('O computador jogou Pedra')
    elif computador == 2:
        print('O computador jogou Papel')
    else:
        print('O computador jogou Tesoura')

    if computador == 1 and humano == 1:
        print('Empate!')
        empate = empate +1
    elif computador == 1 and humano == 2:
        print('Você ganhou!')
        pontos_humano = pontos_humano + 1
    elif computador == 1 and humano == 3:
        print('Computador ganhou!')
        pontos_computador = pontos_computador + 1
    elif computador == 2 and humano == 2:
        print('Empate!')
        empate = empate+1
    elif computador == 2 and humano == 3:
        print('Você ganhou!')
        pontos_humano = pontos_humano + 1
    elif computador == 2 and humano == 1:
        print('Computador ganhou!')
        pontos_computador = pontos_computador +1
    elif computador == 3 and humano == 3:
        print('Empate!')
        empate = empate+1
    elif computador == 3 and humano == 1:
        print('Você ganhou!')
        pontos_humano = pontos_humano + 1
    elif computador == 3 and humano == 2:
        print('Computador ganhou!')
        pontos_computador = pontos_computador +1
print('\n')
print('-' * 30)
print('Você fez {} pontos\n'
      'O computador fez {} pontos\n'
      '{} empate(s)'.format(pontos_humano,pontos_computador,empate))
print('-' * 30)
print('-' * 30)
if pontos_humano > pontos_computador:
    print('Você ganhou do computador')
elif pontos_humano < pontos_computador:
    print('O computador ganhou!')
else:
    print('Ficou empatado!')
print('-' * 30)
print('-' * 30)