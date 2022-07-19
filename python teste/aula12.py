nome = str(input('Seu nome:')).strip().upper()


if nome == 'LUCAS':
    print('Nome lindo da muléstia')

elif nome == 'PEDRO' or nome=='MARIA':
    print('Seu nome é comum no Brasil')

elif nome in 'ANA CLÁUDIA RONALDA':
    print('Lindo nome')

else:
    print('nome feiii')

print(f'tenha um bom dia {nome.lower().title()}')