# Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
# 1 a 20 polegadas. A conversão entre estas duas unidades é dada por: polegada =
# centímetro × 2,54
polegadas = 1
while 1<= polegadas <= 20:
    centimetros = polegadas / 2.54
    print(polegadas, 'polegadas =', centimetros, 'centímetros')
    polegadas += 1