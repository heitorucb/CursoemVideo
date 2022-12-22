velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
  print('Voce foi multado!')
  multa = (velocidade-80)*7
  print('A multa é: {}'.format(multa))
else:
  print('Você está dentro da velocidade da via!')
