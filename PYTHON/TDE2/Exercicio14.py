# entradas
numeroum = int(input('Insira um número inteiro'))
numerodois = int(input('Insira um número inteiro'))
terceironumero = int(input('Insira um número inteiro'))
# Saídas
if numeroum < numerodois < terceironumero:
    print(terceironumero)
elif numerodois < numeroum < terceironumero:
    print(terceironumero)
elif terceironumero < numerodois < numeroum:
    print(numeroum)
elif terceironumero < numeroum < numerodois:
    print(numerodois)
elif numerodois < terceironumero < numeroum:
    print(numeroum)
else:
    print(numerodois)