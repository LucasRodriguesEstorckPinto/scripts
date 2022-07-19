v = int(input('Digite a distância da sua viagem em km: '))

if v <= 200:
    print(f'Sua passagem irá custar R${v * 0.50:.2f}')
else:
    print(f'Sua passagem irá custar R${v * 0.45:.2f}')
print('Tenha uma boa viagem')