print('CALCULO DE DESCONTO')
p = float(input('INSIRA O VALOR AQUI:R$'))
d1 = int(input('Qual a porcentagem de desconto?:'))
d = p * (d1 / 100)
f = p - d

print(f'Você terá um desconto de: \033[1;32m{d:.2f}\033[m reais')
print(f'O novo preço do produto é: \033[1;31m{f:.2f}\033[m reais')
