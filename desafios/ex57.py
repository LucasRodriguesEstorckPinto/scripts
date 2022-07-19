n = str(input('digite seu sexo: [M/F] ')).strip().upper()
while n not in 'MF':
    n = str(input('digite seu sexo \033[31mCORRETAMENTE\033[m: [M/F] ')).strip().upper()
print('Sexo registrado com sucesso')