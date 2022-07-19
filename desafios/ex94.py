tor = []
temp = {}
som = 0
mu = []
while True:
    temp['nome'] = str(input('Nome: ')).strip().lower().title()
    h = temp['sexo'] = str(input('sexo [M/F]: ')).strip().upper()
    while h not in 'MF':
        h = temp['sexo'] = str(input('sexo [M/F]: ')).strip().upper()
    if h=='F':
        mu.append(temp['nome'])
    temp['idade'] = int(input('Idade: '))
    som = som + temp['idade']
    tor.append(temp.copy())
    temp.clear()
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while r not in 'SN':
        r = str(input('DIGITE CORRETAMENTE --Deseja continuar? [S/N] ')).upper().strip()
    if r=='N':
        break
media = som/len(tor)
print('-='*30)
print(f'- Foram cadastradas {len(tor)} pessoas')
print(f'- A média de idade de todas as {len(tor)} pessoas cadastradas é de {media:5.2f} anos')
print(f'- As {len(mu)} mulheres presentes no grupo são: ',end='')
for p in mu:
    print(p,end='...')
print()
print('As pessoas com a idade acima da média são: ')
for c in range(0,len(tor)):
    if tor[c]['idade']>media:
        print(f' =>{tor[c]["nome"]} com {tor[c]["idade"]} anos',)
print('<< ENCERRADO >>')

