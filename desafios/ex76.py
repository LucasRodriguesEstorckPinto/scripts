s = 0
itens = ('Caderno', 13, 'Lápis', 2, 'Borracha', 1.50, 'Caneta', 2,
         'Lego Star Wars', 450, 'Carrinno de boneca', 200, 'Livro', 50)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for pro in range(0, len(itens)):
    if pro % 2 == 0:
        print(f'{itens[pro]:.<30}', end='')
    if pro % 2 == 1:
        print(f'R$ {itens[pro]:.2f}')
        s = s + itens[pro]
print('=' * 40)
print(f'O valor total a se pagar é: R$ {s:.2f}')
