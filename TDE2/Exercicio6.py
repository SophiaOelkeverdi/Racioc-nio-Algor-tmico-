# Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 -
# feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
# seguintes fórmulas:
# a. para homens: p = (72.7 * h) - 58
# b. para mulheres: p = (62.1 * h) - 44.7
altura = float(input('Digite aqui a altura desejada'))
sexo = int(input('Digite 1 se o sexo for feminino e digite 2 se o sexo for masculino'))
# processamento

# saida
if sexo == 1:
    print((72.7 * altura) - 58)
else:
    print((62.1 * altura) - 44.7)