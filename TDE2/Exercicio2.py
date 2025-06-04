# Apartir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
# a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
# de motorista ou não, informando sua situação.


# Entradas
anodenascimento = int(input('Informe o ano de nascimento'))
# Processamento
idade = 2023 - anodenascimento
# Saídas
print('A idade que a pessoa completara vai ser de:', idade)
if idade >= 18:
    print('A pessoa pode fazer a carteira de motorista')
else:
    print('A pessoa ainda nao pode fazer a carteira de motorista')