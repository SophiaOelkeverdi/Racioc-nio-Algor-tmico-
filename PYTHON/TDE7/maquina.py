matriz = [[1, 3.75,  2],
          [2, 3.67,  5],
          [3, 9.96,  1],
          [4, 1.25,  100],
          [5, 13.99, 2]]

nome_produtos = {
    1: "Coca-Cola",
    2: "Pepsi",
    3: "Monster",
    4: "Café",
    5: "Redbull"
}

estoqueTroco = {
    100.0: 5,
    50.0: 15,
    20.0: 22,
    10.0: 17,
    5.0: 22,
    2.0: 26,
    1.0: 35,
    0.5: 49,
    0.25: 50,
    0.1: 61,
    0.05: 37
}

def calcularTroco(valor, valor_inserido):
    troco = round(valor_inserido - valor, 2)
    troco_usado = {}
    for moeda in sorted(estoqueTroco.keys(), reverse=True):
        quantidade_necessaria = int(troco // moeda)
        quantidade_usada = min(quantidade_necessaria, estoqueTroco[moeda])
        if quantidade_usada > 0:
            troco_usado[moeda] = quantidade_usada
            troco -= round(quantidade_usada * moeda, 2)
    if troco > 0:
        return None
    for moeda, qtd in troco_usado.items():
        estoqueTroco[moeda] -= qtd
    return troco_usado

def modo_admin():
    senha = input("Digite a senha para entrar no modo administrador: ")
    if senha != "adm2415":
        print("Senha inválida!")
        return
    print("""Selecione o modo que deseja operar:
          [1] Cadastrar
          [2] Editar
          [3] Remover""")
    operacao = int(input('Insira o modo que deseja operar: '))
    if operacao == 1:
        produto_novo = input('Digite o nome da nova bebida: ')
        id_novo = int(input('Insira o novo ID: '))
        preco_novo = float(input('Insira o preço do novo produto: '))
        estoque_novo = int(input('Insira o estoque inicial: '))
        nome_produtos[id_novo] = produto_novo
        matriz.append([id_novo, preco_novo, estoque_novo])
    elif operacao == 2:
        id_editar = int(input('ID do produto que deseja editar: '))
        for i, linha in enumerate(matriz):
            if linha[0] == id_editar:
                novo_nome = input('Novo nome do produto: ')
                novo_preco = float(input('Novo preço: '))
                novo_estoque = int(input('Novo estoque: '))
                matriz[i][1] = novo_preco
                matriz[i][2] = novo_estoque
                nome_produtos[id_editar] = novo_nome
                print('Produto atualizado!')
                break
        else:
            print("Produto não encontrado.")
    elif operacao == 3:
        id_remover = int(input('ID do produto a ser removido: '))
        for i, linha in enumerate(matriz):
            if linha[0] == id_remover:
                del matriz[i]
                nome_produtos.pop(id_remover, None)
                print("Produto removido.")
                break
        else:
            print("Produto não encontrado.")
    else:
        print("Opção inválida.")

while True:
    try:
        modo = int(input('''Insira o modo:
[1] Visitante
[2] Administrador
Sua opção: '''))
        if modo == 2:
            modo_admin()
        elif modo == 1:
            for linha in matriz:
                id_produto = linha[0]
                nome = nome_produtos.get(id_produto, "Nome desconhecido")
                preco = linha[1]
                estoque = linha[2]
                print(f"[{id_produto}] {nome} - R${preco:.2f} |")
            while True:
                id_digitado = int(input('ID desejado: '))
                produto_encontrado = None
                for linha in matriz:
                    if linha[0] == id_digitado:
                        produto_encontrado = linha
                        break
                if produto_encontrado:
                    break
                else:
                    print("Selecione a bebida disponível:")
            nome = nome_produtos[produto_encontrado[0]]
            valor = produto_encontrado[1]
            estoque = produto_encontrado[2]

            print(f"Produto: {nome} | Preço: R${valor} | Estoque: {estoque}")

            while True:
                valor_inserido = float(input('Insira o valor inserido na máquina: '))
                if valor_inserido >= valor:
                    print(f"Você vai pagar R${valor}")
                    troco = calcularTroco(valor, valor_inserido)
                    if troco is None:
                        print("Não há troco suficiente na máquina. Compra cancelada.")
                    else:
                        print("Troco: ")
                        for moeda, qtd in troco.items():
                            print(f"R${moeda:.2f} x {qtd}")
                        produto_encontrado[2] -= 1  # atualiza estoque
                    break
                else:
                    print("Valor insuficiente. Insira um valor maior.")
        else:
            print("Opção inválida.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
