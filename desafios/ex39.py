from datetime import date
a = int(input('Digite o ano que você nasceu:'))
atual = date.today().year
b = atual - a
r = 'pode'

print(f'Você tem {b} anos em {atual}')
if b == 18:
    r = 'Hora de se alistar'
    print(r)
elif b < 18:
    r = 'Você ainda vai se alistar'
    print(r)
    print(f'Falta {18-b} anos para o alistamento')
    print(f'Você vai se alistar em {(18-b)+atual}')
elif b > 18:
    r = 'Já passou a hora de se alistar'
    print(r)
    print(f'Você está {b-18} anos atrasado seu nóia')
    print(f'Seu alistamento foi em {atual-(b-18)}')




