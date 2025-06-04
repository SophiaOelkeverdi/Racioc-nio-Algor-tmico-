m = []
nLinhas = int(input('Entre com a qtde de linhas: '))
nColunas = int(input('Entre com a qtde de colunas: '))

# linha_matriz = [] # se colocar aqui acaba alterando as linhas, não vai criar nenhum vetor diferente, mesma linha sempre contruida
for linha in range(nLinhas):
    lista_matriz = [] # cria 5 vetores diferentes
    for coluna in range(nColunas):
        lista_matriz.append(1)
    m.append(lista_matriz)

m[2][3] = 10
for linha in range(nLinhas):
    for coluna in range(nColunas):
            print(m[linha][coluna], end=' ')
            print(' ')
