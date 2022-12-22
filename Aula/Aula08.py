import emoji
import math

print(emoji.emojize('Python é :thumbs_up:'))
print(emoji.emojize("Olá, Mundo :polegar_para_cima:", language='pt'))

print(emoji.demojize("Olá, Mundo 👍", language='pt'))
print(emoji.demojize("Python é 👍", language='pt'))


teste = float(input('Digite um valor: '))
print(math.ceil(teste))
print(int(teste))

raiz = math.sqrt(teste)
print(raiz)
