"""Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados."""
from random import sample
import numpy as np
matriz = []
linha = 4
coluna = 4

for i in range(1):
    lista_matriz = []
    for j in range(1):
        num = sample(range(100,999),16)
    matriz.append(num)

matriz = np.array(matriz).reshape(4,4)
maior_elemento = matriz.max()
linha_maior_elemento = np.where(matriz == maior_elemento)[0][0]
menor_elemento_linha = matriz[linha_maior_elemento].min()

print('A matriz é: ')
print(matriz)

print('O maior elemento é:',maior_elemento)
print('O menor elemento é: ',menor_elemento_linha)
