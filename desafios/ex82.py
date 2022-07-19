t = []
p = []
i = []
j = 0
while True:
    j = t.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('DIGITE CORRENTAMENTE-- Deseja continuar? [S/N]')).strip().upper()[0]
    if r=='N':
        break
for j in t:
    if j%2==0:
        p.append(j)
    else:
        i.append(j)
print('=='*30)
print(f'Você digitou os seguintes números: {t}')
print(f'A lista com apenas os números pares: {p}')
print(f'E a lista apenas com os números ímpares: {i}')