tot = c = p = m = cont = 0
menor = ''
print('---GERENCIADOR DE COMPRAS---')
while True:
    n = str(input('Digite o produto a ser comprado: ')).strip().lower().capitalize()
    p = float(input('Qual é o preço do produto? R$'))
    tot = tot + p
    e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while e not in 'SN':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont = cont + 1
    if p>1000:
        c = c + 1
    if cont==1 or p<m:
        menor = n
        m = p
    if e in 'N':
        break
print(f'O total gasto na compra foi de R${tot:.2f}\n'
      f'{c} produtos custam mais de MIL REAIS\n'
      f'{menor} é o produto mais barato, custando R${m:.2f}')