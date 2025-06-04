"""Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas."""
lista = []
i = 0
v = 0
for i in range(1,11):
    num = int(input('Insira um valor: '))
    lista.append(num)
n2 = int(input('Insira o valor que deseja procurar'))
v = 0
posicoes = []
for i in range(len(lista)):
    if lista[i] == n2:
        v += 1
        posicoes.append(i)
if v > 0:
    print('O valor de ocorrências é', v)
    print('O valor das posições é: ', posicoes)