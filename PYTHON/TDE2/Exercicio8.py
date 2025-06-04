# entradas
minutos = int(input('Insira aqui o tempo em minutos em que o veiculo permaneceu no estacionamento'))
if minutos <= 60:
    print('O valor a ser pago no estacionamento sera de R$8,00')
else:
    print('O valor pago pelo estacionamento em reais será de', ((minutos - 60) / 15) * 1.5 + 8)