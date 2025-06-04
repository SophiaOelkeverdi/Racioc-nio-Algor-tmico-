# Entradas
idade = int(input('Informe a idade do nadador participante: '))
# Saídas
if 5 <= idade <= 7:
    print('O nadador se encontra na categoria Infantil A.')
elif 8 <= idade <= 10:
    print('A categoria do nadador é Infantil B.')
elif 11 <= idade <= 13:
    print('A categoria do nadador é Juvenil A.')
elif 14 <= idade <= 17:
    print('A categoria do nadador é Juvenil B')
elif idade < 5:
    print('O nadador não pode participar da competição.')
else:
    print('A categoria do nadador é Adulto')