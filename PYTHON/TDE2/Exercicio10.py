# Entradas
massa = float(input('Informe a massa necessária para o calculo: '))
altura = float(input('Informe a altura necessária para o calculo: '))
# processamento
imc = massa / altura ** 2
# Saídas
if imc < 18.5:
    print('A pessoa se encontra a baixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('A pessoa se encontra no peso ideal.')
elif 25 <= imc < 30:
    print('A pessoa se encontra acima do peso.')
else:
    print('A pessoa se encontra no nível de obesidade')