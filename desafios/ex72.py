v = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    d = int(input('Digite um número entre 0 e 20: '))
    if 0 <= d <= 20:
        break
print(f'Você digitou o número {v[d]}')
