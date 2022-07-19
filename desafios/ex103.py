def ficha(n='', gols=''):
    """
    Printa uma ficha do jogador
    :param n: Nome do jogador
    :param gols: Número de gols
    :return: Não retorna nenhum valor
    """
    if n == '':
        n = '<DESCONHECIDO>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {n},fez {gols} gol(s) no campeonato')


print('__'*20)
n1 = str(input('Nome do jogador: ')).strip().lower().title()
n2 = str(input('Número de gols: ')).strip()
ficha(n1,n2)