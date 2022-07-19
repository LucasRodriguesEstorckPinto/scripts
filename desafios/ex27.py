n = str(input('DIGITE SEU NOME COMPLETO:')).strip()
print(f'Seu nome completo é {n.title()}')
a = n.split()
print(f'Seu primeiro nome é: {a[0].title()}')
a.reverse()
print(f'Seu ultimo nome é: {a[0].title()}')

