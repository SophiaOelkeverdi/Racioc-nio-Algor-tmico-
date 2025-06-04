# matriz quadrada: mesmo número de linhas e colunas
# matriz é um vetor de vetores

# print(m[1][2])
# para acessar o elememto, coloque o indice da linha (começa em 0)
# depois, coloque o indice da coluna (começa em 0)

m = [[1,2,3,7,5],
     [4,5,6,7,9],
     [7,8,9,2,3],
     [3,4,5,6,7],
     [9,8,7,6,5]]

# len(m) retorna a quantidade de linhas
# len(m[0]) retorna a quantidade de colunas

# se atentar aos indices!!

# m[2][2] = 54 # trocar valores na matriz


# para percorrer a matriz: um for com as linhas e dentro o de colunas
for linha in range(len(m)):
    for coluna in range(len([0])):
        print(m[coluna][linha])
print('')

# elementos que tem o mesmo indice de coluna e de linha são os da diagonal da matriz

print('Diagonal')
for linha in range(len(m)):
    for coluna in range(len([0])):
        if coluna == linha:
         print(m[coluna][linha])
print('')

# abaixo da diagonal se forma um triângulo de números inferiror e em cima, um triângulo superior

print('Triângulo Superior')
for linha in range(len(m)):
    for coluna in range(len([0])):
        if coluna > linha:
         print(m[coluna][linha],end=' ')
        else:
           print(0,end=' ')
print('')

print('Triângulo Inferior')
for linha in range(len(m)):
    for coluna in range(len([0])):
        if coluna < linha:
         print(m[coluna][linha],end=' ')
        else:
           print(0,end=' ')
print('')