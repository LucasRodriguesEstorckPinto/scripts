a = float(input('QUAL É A VELOCIDADE ATUAL DO CARRO? '))
print(f'{a} km/h')

if a > 80 :
    print(f'Você foi multado por exceder o limite de velocidade em {a - 80} km/h')
    print(f'Sua multa foi de \033[1;31m{(a - 80) * 7:.2f}\033[m reais')

else:
    print('\033[32mVelocidade segura\033[m')
print('Dirija com segurança')
