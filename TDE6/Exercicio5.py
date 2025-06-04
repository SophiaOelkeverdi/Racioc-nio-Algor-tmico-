"""Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação."""
from random import randint
matriz = []
vetor_pares = []
vetor_impar = []
matriz_final = []
k = 0
for i in range(15):
    lista_matriz = []
    for j in range(7):
        num = randint(10,99)
        lista_matriz.append(num)
    matriz.append(lista_matriz)
print('A matriz original é: ')
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='|')
    print()

for linha in range(len(matriz)):
    for coluna in range(len([0])):
        if num % 2 == 0:
            vetor_pares.append(num)
        else:
            vetor_impar.append(num)
print('')

n = vetor_pares + vetor_impar

for i in range(15):
    linha_matriz_final = []
    for j in range(7):
        linha_matriz_final.append([k])
        k += 1
    matriz_final.append(linha_matriz_final)

print('A matriz original é: ')
for i in range(len(matriz_final)):
    for j in range(len(matriz_final[0])):
        print(matriz_final[i][j], end='|')
    print()