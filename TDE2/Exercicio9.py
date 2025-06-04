# Entradas
idade = int(input('Informe a idade da pessoa: '))
# Saídas
if 18 <= idade <= 65:
    print('A pessoa é um eleitor obrigatorio.')
elif 16 <= idade < 18:
    print('A pessoa é um eleitor facultativo')
elif idade > 65:
    print('A pessoa é um eleitor')
else:
    print('A pessoa ainda não tem permissão a ser um eleitor')