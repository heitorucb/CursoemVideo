frase = 'Curso em Vídeo Python'
print(len(frase))
print(frase.count('o'))
print(frase[1:13])
print(frase[1:20:3]) #fatia a string do indice 1 ao 20 pulando 3 casas
print('Frase.count()' + str(frase.find('e', 0, 13)))

print('Curso' in frase)
replace = frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android'))
print(frase)
print(replace)
frase_upper=frase.upper()
print(frase_upper)
print(frase.lower())
print(frase.capitalize())
print(frase.title())
strip = '    Digitei vários espaços no começo e no final   '
print(strip)
print(strip.strip())
split = frase.split()
print(split)
print('-'.join(split))
