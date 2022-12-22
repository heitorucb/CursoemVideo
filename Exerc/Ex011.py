largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f}m²'.format(largura, altura, largura*altura))
print('Para pintar essa parede, você irá precisar de {:.3f}l'.format((largura*altura)/2))