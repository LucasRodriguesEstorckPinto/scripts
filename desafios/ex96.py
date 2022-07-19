print('Controle de terrenos')
print('_' * 20)


def area(a, b):
    area = a*b
    print(f'A área de um terreno {a}x{b} é de {area}m².')


area(float(input('LARGURA (m): ')),
     float(input('COMPRIMENTO (m): ')))
