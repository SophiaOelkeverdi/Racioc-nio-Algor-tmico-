# Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
# valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
# intervalo, ou seja, intervalo aberto.
limiteInicial = int(input('Informe o limite inicial de número: '))
limiteFinal = int(input('Informe o limite final para o número: '))
numero = 1 + limiteInicial
while limiteInicial < numero < limiteFinal:
    resto = numero % 3
    if resto == 0:
        print(numero)
        numero += 3
    else:
        print(numero)
        numero += 1