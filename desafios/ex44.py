a = float(input('Digite o valor do produto: R$'))

print('Escolha o método de pagamento')
print('[1] À VISTA DINHEIRO/CHEQUE')
print('[2] À VISTA NO CARTÃO')
print('[3] 2x NO CARTÃO')
print('[4] 3x OU MAIS NO CARTÃO')
b = int(input('Método: '))

if b == 1:
    print(f'O desconto será de 10%, logo, o novo valor é R$ {a - (10 / 100) * a:.2f}')
elif b == 2:
    print(f'O desconto será de 5%, o novo valor será R$ {a - (5 / 100) * a:.2f}')
elif b == 3:
    print(f'Sem descontos, o valor permace em R$ {a}')
elif b==4:
    print(f'O desconto será de 20%, o novo valor será de R$ {a - (20/100) *a:.2f}')
    tot = int(input('Quantas parcelas?'))
    parcela = (a - (20/100) *a)/tot
    print(f'Sua compra sera parcelada em {tot}x de R${parcela:.2f}')
