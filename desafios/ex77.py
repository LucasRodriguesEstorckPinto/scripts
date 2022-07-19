tupla = ('pinta','amor','carinho','carro','viajar','estudar','python')
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos: ',end=' ')
    for p in c:
        if p in 'aeiou':
            print(f'{p}',end=' ')