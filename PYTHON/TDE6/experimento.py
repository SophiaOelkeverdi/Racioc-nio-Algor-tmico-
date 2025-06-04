import random

matriz = []

for i in range(5):
    linha_matriz = []
    for j in range(5):
        linha_matriz.append(random.sample(range(10, 99), 1))
    matriz.append(linha_matriz)

print("Matriz Original: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

print("Matriz Versão A: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 2 or j == 2:
            print(matriz[i][j], end = ' | ')
        else:
            print("  - ", end = ' | ')
    print()