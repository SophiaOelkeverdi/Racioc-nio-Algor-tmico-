# Entradas
precodoproduto = float(input('Informe o preço do produto que vai ser comprado: '))
mododepagamento = int(input('Digite 1 para pagamento a vista, digite 2 para parcelar em 2 vezes, digite 3 para parcelar 3 vezes e digite 4 para parcelar em 4 vezes'))
# Saídas
if mododepagamento == 1:
    print('O preço do produto vai ser igual a:', precodoproduto * 0.92)
elif mododepagamento == 2:
    print('O preço do produto vai ser igual a: ', precodoproduto * 0.96 / 2)
elif mododepagamento == 3:
    print('O preço do produto vai ser igual a: ', precodoproduto / 3)
elif mododepagamento == 4:
    print('O preço do produto vai ser igual a: ', precodoproduto * 1.04 / 4)