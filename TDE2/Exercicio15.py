# Entradas
primeironumero = float(input('Insira um número aqui:'))
segundonumeto = float(input('Insira outro número aqui:'))
terceironumero = float(input('Insira outro número aqui:'))
#Saida
if primeironumero < segundonumeto < terceironumero:
    print(primeironumero , segundonumeto , terceironumero)
elif segundonumeto < primeironumero < terceironumero:
    print(segundonumeto , primeironumero, terceironumero)
elif terceironumero < segundonumeto < primeironumero:
    print(terceironumero , segundonumeto, primeironumero)
elif terceironumero < primeironumero < segundonumeto:
    print(terceironumero , primeironumero , segundonumeto)
elif segundonumeto < terceironumero < primeironumero:
    print(segundonumeto , terceironumero, primeironumero)
else:
    print(primeironumero , terceironumero, segundonumeto)