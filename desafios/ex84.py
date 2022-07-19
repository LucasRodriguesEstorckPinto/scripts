pessoas = []
dado = []
cont = 0
pmai = []
pmenor = []
while True:
    dado.append(str(input('Digite o nome: ').strip().title()))
    dado.append(float(input('Digite o peso: KG')))
    cont = cont + 1
    pessoas.append(dado[:])
    dado.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('DIGITE CORRENTAMENTE --Deseja continuar? [S/N] ')).strip().upper()
    if r=='N':
        break
print('=='*20)
print(f'Foram registradas {cont} pessoas')
for p in pessoas:
    if p[1]>=70:
        pmai.append(p[0])
    elif p[1]<=70:
        pmenor.append(p[0])
print(f'As pessoas com os menores pesos são {pmenor}')
print(f'As pessoas com os maiores pesos são {pmai}')
