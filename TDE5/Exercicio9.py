"""Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores"""
vLido = []
vPares = []
vImpares = []
vZero = []
i = 0
for i in range(1,11):
    num = int(input('Insira um valor: '))
    vLido.append(num)
    if num % 10 == 0:
        vZero.append(num)
    elif num % 2 == 0:
        vPares.append(num)
    else:
        vImpares.append(num)
print(vLido)
print('Os números pares são:', vPares)
print('Os números ímpares são:', vImpares)