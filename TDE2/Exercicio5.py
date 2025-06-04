# m uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
# cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. Elabore
# um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.
# entradas
numeroDeCopias = int(input('Digite aqui o número de cópias'))
if numeroDeCopias < 100:
    print(numeroDeCopias * 0.25)
else:
    print(numeroDeCopias * 0.2)