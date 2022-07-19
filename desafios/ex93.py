dic = {}
gols = []
tot = 0
dic['nome'] = str(input('Nome do jogador: ')).lower().strip().title()
h = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0,h):
    n =(int(input(f'Quantos gols na partida {c+1}? ')))
    gols.append(n)
    tot = tot + n
dic['gols'] = gols
dic['total'] = tot
print('-='*30)
print(dic)
print('-='*30)
for k,v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dic["nome"]} jogou {h} partidas')
for c in range(0,h):
    print(f'  => Na partida {c+1}, fez {dic["gols"][c]} gols.')
