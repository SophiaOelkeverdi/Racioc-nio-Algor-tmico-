# Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
# de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
# quilômetros.
milhas = 20
while 20 <= milhas <= 160:
    kilometros = milhas / 1.609344
    print(milhas, 'polegadas =', kilometros, 'centímetros')
    milhas += 1