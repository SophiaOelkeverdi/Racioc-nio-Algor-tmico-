"""Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve."""
from random import sample
mega = []
pessoa = []
igual = []
num = 0
i = 0
v = 0
p = 0
for i in range(1,2):
    num = sample(range(1,61),6)
    mega.append(num)
for i in range(1,7):
    sort = int(input('Insira o valor de um número entre (1 e 60): '))
    if sort != pessoa:
        pessoa.append(sort)
    else:
        print('Não é possível colocar o número repetido: ')
for i in range(1,2):
    if set(num) & set(pessoa):
        p += 1
    else:
        p += 0
print(num)
print('Os valores que vão ser iguais são:',set(num) & set(pessoa))
print('A quantidade de acertos foi: ',p)