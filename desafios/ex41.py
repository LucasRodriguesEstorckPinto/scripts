from datetime import date
a = int(input('Ano de nascimento:'))
ano = date.today().year
ida = ano-a
cat = 'mirim'

if 0 <= ida <= 9:
    cat = 'MIRIM'
elif 9 < ida <= 14:
    cat = 'INFANTIL'
elif 14 < ida <= 19:
    cat = 'JUNIOR'
elif 19 < ida <= 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'

print(f'O atleta de {ida} anos se encaixa na categoria \033[31m{cat}\033[m.')