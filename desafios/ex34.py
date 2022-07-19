s = float(input('Digite aqui o seu salário para o aumento ser calculado: R$ '))
a = (s*10)/100
b = (s*15)/100
if s>1250:
    print(f'Com o aumento de 10%,seu novo salário será R${s+a:.2f}')
if s<=1250:
    print(f'Com o aumento de 15%,seu novo salário será R${b+s:.2f}')