distancia = int(input('Digite uma distância de viagem:'))
if distancia <= 200:
    print('Sua viagem irá custar R${:.2f}'.format(distancia*0.50))
else:
    print('Sua viagem irá custar R${:.2f}'.format(distancia*0.45))