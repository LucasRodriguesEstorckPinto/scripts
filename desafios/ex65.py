print('Nesse programa, você vai digitar varios números e será mostrado o maior e o menor e a média')
n = 0
e ='S'
c = 0
s = 0
maior = 0
menor = 999999999999999999999999999
while e!='N':
    n = (int(input('Digite algum número: ')))
    e = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    c = c + 1
    s = s + n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
media = s/c
print(f'A média entre todos os {c} números digitados é: {media:.2f}')
print(f'O maior número é {maior} e o menor é {menor}')

