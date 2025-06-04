# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
# algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
# que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
# para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
# (quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
# R$1.000). Considere o câmbio do dia.
montanteMoeda = float(input('Insira o valor do montante que quer da moeda: '))
moeda = int(input('Insira um para dolar, dois para libras, três para euros: '))
valoremrealdedolar = montanteMoeda * 5.68
valoremrealdelibras = montanteMoeda * 7.34
valoremrealdeeuros = montanteMoeda * 6.13
if moeda == 1:
    print('O valor em real será de: ', valoremrealdedolar)
elif moeda == 2:
    print('O valor em real será de: ', valoremrealdelibras)
elif moeda == 3:
    print('O valor em real será de: ', valoremrealdeeuros)
if valoremrealdedolar > 1000:
    print('O valor final é de: ', valoremrealdedolar * 1.05)
else:
    print('O valor é de:', valoremrealdedolar * 1.03)
if valoremrealdelibras > 1000:
    print('O valor é de: ', valoremrealdelibras * 1.05)
else:
    print('O valor final é de: ', valoremrealdelibras * 1.03)
if valoremrealdeeuros > 1000:
    print('O valor é de: ', valoremrealdeeuros * 1.05)
else:
    print('O valor é de: ', valoremrealdeeuros * 1.03)