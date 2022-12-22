import math

catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hip = math.sqrt((math.pow(catop,2)+math.pow(catadj,2)))
print('O valor da hipotenusa é: {}'.format(hip))
hipot = math.hypot(catop,catadj)
print(hipot)
