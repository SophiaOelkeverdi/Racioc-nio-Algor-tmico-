# Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
# qual o valor da soma e da média aritmética do conjunto.
soma = 0
contador = 0
while contador < 10:
    nun = int(input('Insira um número inteiro: '))
    soma = soma + nun
    contador += 1
    print('Soma', soma, 'Média Aritmética', (soma/10))