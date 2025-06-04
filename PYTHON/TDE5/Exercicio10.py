"""Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
depois, os números impares. Mostre o vetor antes de depois da modificação."""
vetor = []
vPar = []
vImpar = []
i = 0
for i in range(1,11):
    num = int(input('Insira um valor:'))
    if num != 0:
        vetor.append(num)
        if num % 2 == 0:
            vPar.append(num)
        else:
            vImpar.append(num)
print('Os números são:', vetor)
print('Os múmeros pares e ímpares em ordem são:', (vPar + vImpar))