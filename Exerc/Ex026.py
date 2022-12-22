frase = str(input('Digite uma frase: ')).lower().strip()
print('O A aparece {} vezes'.format(frase.count('a')))
print('A primeira aparição do A é na posição {}'.format(frase.find('a')+1))
print('A última aparição do A é na posição {}'.format(frase.rfind('a')+1))
