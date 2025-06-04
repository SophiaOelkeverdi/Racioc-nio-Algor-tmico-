# Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.
i = 0
soma = 0
lista = []
for i in range(0,3):
    num = int(input('Insira um valor: '))
    i += 1
    lista.append(num)
soma = lista[1] + lista[2]
if lista[0] > soma:
    print('Os números são {} {} {}, e as somas do {} {} é menor que o {}'. format(lista[0],lista[1],lista[2],lista[1],lista[2],lista[0]))
else:
    print('A soma dos números {}, {} é maior que o {}'.format(lista[1], lista[2], lista[0]))
    