"""A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
São Paulo é de 408 km.
Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.
"""
vetor_cidade = ['Curitiba', 'Florianópolis', 'Porto Alegre', 'São Paulo', 'Rio de Janeiro']
matriz = [[0,310,716,408,852],
          [310,0,470,705,1144],
          [408,705,1119,0,429],
          [852,1144,1553,429,0]]
velocidade = int(input('Insira o valor da velocidade que a pessoa vai andar: '))
print('''Lista de cidades:\n[0] Curitiba\n[1] Florianópolis\n[2] Porto Alegre\n[3] São Paulo\n[4] Rio de Janeiro ''')
cidade1 = int(input(''' Insira o valor da cidade desejada: '''))
cidade2 = int(input('''Insira o valor da cidade desejada: '''))

print('A distância entre as cidades escolhidas é: ',matriz[cidade1][cidade2])

distancia = matriz[cidade1][cidade2]
tempo = distancia / velocidade

print('O tempo que vai levar para percorrer as duas cidade é {}. '.format((tempo * 60)))


