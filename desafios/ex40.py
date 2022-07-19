n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2) / 2
d = 7 - m
print(f'nota final={m:.1f} ')
if m < 5:
    print(f'Aluno \033[31mREPROVADO\033[m por {d} pontos')
elif 5 <= m <= 6.9:
    print(f'Aluno em \033[33mRECUPERAÇÃO\033[m por {d} pontos')
elif m >= 7:
    print('Aluno \033[32mAPROVADO\033[m com excelência')
