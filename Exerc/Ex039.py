from datetime import date
ano = int(input('Qual o ano do seu nascimento: '))
ano_atual = date.today().year
if ano_atual - ano == 18:
    print('Voce já pode se alistar.')
elif ano_atual - ano < 18:
    print('Você ainda não pode se alistar, pois falta(m) {} ano(s) ainda'.format(18 - (ano_atual-ano)))
else:
    print('Você deve se alistar comm urgência pois já se passaram {} anos do prazo normal'.format((ano_atual-ano) - 18))