#  IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
# IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
# e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
# apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
# não esteja, calcule sua massa máxima considerada normal
massa = float(input('Insira aqui a massa desejada: '))
altura = float(input('Insira aqui a altura desejada'))
imc = massa / (altura ** 2)
massamaxima = 24.9 * (altura ** 2)
# Saídas
if 18.5 > imc > 25:
    print('Massa máximaa para ser considerada normal é: ', massamaxima)
else:
    print('O imc será:', imc)