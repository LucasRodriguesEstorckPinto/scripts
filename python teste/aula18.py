#galera = [['Lucas',17], ['Naju',16], ['Alice',6], ['Pedrin bala nervosa',35]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos ')
galera = []
dado = []
maior = menor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade.')
        maior = maior + 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor = menor + 1
print(f'Temos {maior} pessoas maiores de idade e {menor} menores de idade')
