from datetime import date

a = int(input('Digite o ano em que você está. Digite 0 para analisar o ano atual:'))
b = a % 4
if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é bissexto')
else:
    print(f'O ano {a} NÃO é bissexto')

print('Obrigado pela preferência')
