# Entradas
peso = float(input('Informe o peso do boxeador em quilogramas: '))
# Processamento
libras = peso * 2.20462262
# Saídas
if libras >= 201.0:
    print('A categoria do boxeador é peso-pesado. ')
elif 176 <= libras <= 200:
    print('A categoria do boxeador é cruzador.')
elif 169 <= libras <= 175:
    print('A categoria do boxeador é Meio-pesado.')
elif 161 <= libras <= 168:
    print('A categoria do boxeador é Super-médio.')
else:
    print('O boxeador não se encaixa em nenhuma das categorias.')