d = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a\n'
      '{}Km\n'
      '{}hm\n'
      '{}dam\n'
      '{}dm\n'
      '{}cm\n'
      '{}mm'
      .format(d,d/1000,d/100,d/10,d*10,d*100,d*1000))
