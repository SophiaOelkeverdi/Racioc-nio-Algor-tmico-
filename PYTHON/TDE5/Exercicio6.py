"""Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular"""
lista = []
lista2 = []
num = int(input("Digite um número: "))
lista.append(num)
raiz =  num **(1/3)
calculo = raiz//1
formula = calculo*(calculo + 1)*(calculo + 2)
lista2.append(calculo)
lista2.append(calculo + 1)
lista2.append(calculo + 2)
print(lista)
print(lista2)
if formula == num:
    print("Esse é um numero triangular")
else:
    print("Não é um numero triangular")
