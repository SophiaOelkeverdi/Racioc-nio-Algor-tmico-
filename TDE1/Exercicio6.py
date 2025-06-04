# Entradas
custoLata = 50
quantidadeLitrosLata = 5
metroPorLitro = 3
altura = float(input('Insira a altura do cilindro em metros'))
raio = float(input('Insira o valor do raio em metros'))
# Processamento
areaTotalCilindro = (altura * (raio * 2 * 3.14)) + (2 * (raio * raio) * 3.14)
quantidadeLatasUsadas = (areaTotalCilindro / metroPorLitro) / quantidadeLitrosLata
valorGastoLatas = quantidadeLatasUsadas * custoLata
# Saída
print('O valor em reais gasto com latas foi de: ', valorGastoLatas)
print('A quantidade de latas usadas foi de: ', quantidadeLatasUsadas)
