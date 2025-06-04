"""Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor"""
matriz = []
vetor = []
linha = 4
coluna = 4

for i in range(linha):
    lista_matriz = [] # cria 5 vetores diferentes
    for j in range(coluna):
        num = int(input('Insira um valor para ser colocado na matriz: '))
        lista_matriz.append(num)
    matriz.append(lista_matriz)
    
print('A matriz é')
for linha in matriz:
    print(linha)

vetor_maior = []
for coluna in range(4):
    maior = matriz[0][coluna]
    for linha in range(1,4):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
    vetor_maior.append(maior)
print('\nVetor com os maiores valores de cada coluna: ')
print(vetor_maior)

media = sum(vetor_maior) / len(vetor_maior)
print('A média é: ', media)