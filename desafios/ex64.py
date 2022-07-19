s = 0
som = 0
c = 0
while s != 999:
    s = int(input('digite um número: '))
    if s != 999:
        som = som + s
        c = c + 1
print(f'Você digitou {c} números e a soma entre todos eles é: {som}')
