'''Leia dois valores reais do teclado, calcular e imprimir na tela:
a) A soma destes valores b) O produto deles c) O quociente entre eles'''
i = 0
lista = []
for i in range(0,2):
    num = int(input('Insira um número: '))
    i += 1
    lista.append(num)
soma = lista[0] + lista[1]
prod = lista[0] * lista[1]
div = lista[0] / lista[1]
print('A soma deles é: ',soma,'O produto deles são: ', prod,'A divisão deles é: ', div)
