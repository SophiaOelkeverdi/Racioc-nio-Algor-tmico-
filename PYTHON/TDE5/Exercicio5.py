# Ler 4 números inteiros e calcular a soma dos que forem par.
lista = []
i = 0
soma = 0
for i in range(0,4):
    num = int(input('Insira um número: '))
    i += 1
    if num % 2 == 0:
        soma += num
print(soma)