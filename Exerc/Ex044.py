preco = float(input('Digite o valor do produto:'))
condicao = int(input('Digite 1 para À vista:\n'
                     'Digite 2 para cartão:\n'
                     'Digite 3 para 2 x no cartão\n'
                     'Digite 4 para 3 x no cartão\n'))
if condicao == 1:
    print('O valor do produto tem 10% de desconto e ficará em R${:.2f}'.format(preco*0.90))
elif condicao == 2:
    print('O valor do produto tem 5% de desncoto e ficará em R${:.2f}'.format(preco*0.95))
elif condicao == 3:
    print('O valor do produto ficará com seu preço normal de R${:.2f}'.format(preco))
elif condicao == 4:
    print('A forma escolhida tem 20% de juros e ficará em R${:.2f}'.format(preco*1.2))
else:
    print('Opção digitada é inválida')
