'''Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.'''
matriz = []
linha = 3
coluna = 3
s = int(input('Insira um valor para multiplicar a matriz: '))
for i in range(linha):
    lista_matriz = []
    for j in range(coluna):
        num = int(input('Insira um valor para ser colocado na matriz: '))
        lista_matriz.append(num * s)
    matriz.append(lista_matriz)
print('A matriz vai ser: ')
print(matriz)