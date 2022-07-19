s = 'j'
n = 0
j = cp = cmu = 0
while True:
    print('_______' * 10)
    print('                    CADASTRE UMA PESSOA')
    print('_______' * 10)
    n = int(input(' Idade : '))
    h = str(input(' Sexo  [M/F]: ')).upper().strip()[0]
    while h not in 'MF':
        h = str(input(' Sexo  [M/F]: ')).upper().strip()[0]
    print('_______' * 10)
    s = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while s not in 'SN':
        s = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if h == 'M':
        j = j + 1
    if n > 18:
        cp = cp + 1
    if h in 'F' and n < 20:
        cmu = cmu + 1
    if s == 'N':
        break
print(f'Um total de {cp} pessoas possuem mais de 18 anos')
print(f'Foram cadastrados {j} homens')
print(f'{cmu} mulheres possuem menos de 20 anos')
