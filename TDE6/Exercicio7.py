'''Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
fornecido.
'''
vetor_cidade = ['Curitiba', 'Florianópolis', 'Porto Alegre', 'São Paulo', 'Rio de Janeiro']
matriz = [[0,310,716,408,852], # Curitiba
          [310,0,470,705,1144], # Florianópolis
          [716,470,0,1119,1553], # Porto Alegre
          [408,705,1119,0,429], # São Paulo
          [852,1144,1553,429,0]] # Rio de Janeiro
print('''Cidades disponíveis:
      Digite o número da cidade: [0] Curitiba\n [1] Florianópolis\n [2] Porto Alegre\n [3] São Paulo\n [4] Rio de Janeiro ''')
roteiro = []
while True:
    entrada = input("Digite o número correspondente a cidade ou FIM para encerrar: ")
    if entrada.upper() == "FIM":
        break
    elif entrada.isdigit():
        indice = int(entrada)
        if 0 <= indice <len(vetor_cidade):
            roteiro.append(indice)
        else:
            print('Indice de cidade inválido: ')
    else:
        print('Entrada inválida. Digite um número ou FIM')
if len(roteiro) < 2:
    print('Necessita de pelo menos duas cidades!')
else:
    print('Roteiro de viagem!\n')
    total = 0
    for i in range(len(roteiro) - 1): # -1 Porque o fim contaria como uma váriavel
        origem = roteiro[i]
        destino = roteiro[i + 1]
        distancia = matriz[origem][destino]
        total += distancia
        print('Cidade origem {} -> Cidade destino{} = Distância {}'.format(vetor_cidade[origem], vetor_cidade[destino],distancia))
        print('Distância percorrida {} em Km'.format(total))