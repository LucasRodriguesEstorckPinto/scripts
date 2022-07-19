dic = {}
gols = []
todos = []
tot = 0
while True:
    dic['nome'] = str(input('Nome do jogador: ')).lower().strip().title()
    h = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for c in range(0, h):
        n = (int(input(f'Quantos gols na partida {c + 1}? ')))
        gols.append(n)
        tot = tot + n
    dic['gols'] = gols[:]
    dic['total'] = tot
    todos.append(dic.copy())
    dic.clear()
    gols.clear()
    tot = 0
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while r not in 'SN':
        r = str(input('DIGITE CORRENTAMENTE-- Deseja continuar? [S/N] ')).upper().strip()
    print('-=' * 30)
    if r == 'N':
        break
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<20}{"Total"}')
print('__'*25)
for c in range(0,len(todos)):
    print(f'{c}    {todos[c]["nome"]:<15}{str(todos[c]["gols"]):<20}{todos[c]["total"]}')
print('__'*25)
while True:
    r = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    print('__'*25)
    if r==999:
        break
    if r<0 or r>=len(todos):
        print(f'ERRO!! Não existe nenhum jogador com o código {r}! Tente novamente')
    if 0 <= r < len(todos):
        print(f'-- LEVANTAMENTO DO JOGADOR {todos[r]["nome"]}')
        for c in range(0,len(todos[r]["gols"])):
            print(f'No jogo {c+1} fez {todos[r]["gols"][c]} gols')
        print('__'*25)
print('<<VOLTE SEMPRE>>')