idade = 0


def voto(ano):
    from datetime import date
    a = date.today().year
    global idade
    idade = a - ano
    if idade >= 0:
        if 16 <= idade < 18 or idade > 65:
            return 'VOTO OPICIONAL'
        elif 18 <= idade <= 65:
            return 'VOTO OBRIGATÓRIO'
        elif idade < 18:
            return 'NÃO VOTA'
    else:
        return 'Não sabemos pois provavelmente essa pessoa veio do futuro ;)'


print('__' * 20)
n = voto(int(input('Em que ano você nasceu? ')))
print(f'Com {idade} anos: {n}.')
