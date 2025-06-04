# Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
# “Valor inválido” para números negativos).
# entradas
numero = int(input('Insira um número inteiro:'))
# processamento
quadrangular = numero ** (1 / 2)
# Saída
if numero < 0:
    print('O valor é invalido')
else:
    print(quadrangular)