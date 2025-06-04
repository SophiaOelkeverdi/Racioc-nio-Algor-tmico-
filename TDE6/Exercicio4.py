"""Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores"""
from random import sample
matriz = []
soma = 0
soma1 = 0
soma2 = 0
soma3 = 0

for i in range(5):
    lista_matriz = []
    for j in range(5):
        lista_matriz.append(sample(range(10,99),1))
    matriz.append(lista_matriz)
print('A matriz original é: ')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='|')
    print()

print('Matriz versão A!!')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 2 or j == 2:
            print(matriz[i][j], end = '|')
            soma += matriz[i][j]
        else:
            print('  - ', end =  '|')   
    print(' ')

print('Matriz versão B!!')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 0 or j == 0 or i == 4 or j == 4:
            print(matriz[i][j], end = '|')
            soma1 += matriz[i][j]
        else:
            print('  - ', end =  '|')   
    print(' ')

    print('Matriz versão C!!')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == (j - 1) or i == (j + 1):
            print(matriz[i][j], end = '|')
            soma2 += matriz[i][j]
        else:
            print('  - ', end =  '|')   
    print(' ')
    print('Matriz versão D!!')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == (j - 1) or i == (j + 1) or j == (i - 3) or j == (i + 3):
            print(matriz[i][j], end = '|')
            soma3 += matriz[i][j]
        else:
            print('  - ', end =  '|')   
    print(' ')
print('Soma da versão A é {}'.format(soma))
print('Soma da versão B é {}'.format(soma1))
print('Soma da versão C é {}'.format(soma2))
print('Soma da versão D é {}'.format(soma3))