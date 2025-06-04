"""A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido."""
lista = []
i = 0
num_max = 0
num_min = 0
amp = 0
for i in range(1,11):
    num = int(input('Insira um valor: '))
    lista.append(num)
    num_max = max(lista)
    num_min = min(lista)
    amp = num_max - num_min
print('O maior número é',num_max)
print('O menor número é',num_min)
print('A amplitude é ',amp)