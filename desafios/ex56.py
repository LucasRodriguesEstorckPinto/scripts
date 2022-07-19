nv = ''
soma = 0
media = 0
idadehmv = 0
contm = 0
for c in range(1, 5):
    print(f'======DADOS DA PESSOA {c}=====')
    n = str(input(f'Nome da pessoa: ')).lower().strip().title()
    i = int(input(f'Idade da pessoa:'))
    s = str(input('SEXO DA PESSOAQ: [M/F]:')).strip().upper()
    soma = soma + i
    if s == 'M' and i > idadehmv:
        idadehmv = i
        nv = n
    if s == 'F' and i < 20:
        contm = contm + 1
media = soma / 4
print('=-'*30)
print(f'\033[31mA media de idade das pessoas é: {media} anos\033[m')
print(f'\033[32mO homem mais velho tem {idadehmv} anos e seu nome é {nv}\033[m')
if contm == 1:
    print('\033[33mApenas uma mulher tem menos de 20 anos')
if contm == 0:
    print('\033[33mTodas as mulheres citadas possuem mais de 20 anos')
if contm > 1:
    print(f'\033[33m{contm} mulheres possuem menos de 20 anos')
