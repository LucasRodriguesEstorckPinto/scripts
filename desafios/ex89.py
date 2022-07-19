from time import sleep
p = []
alu = []
nota = []
while True:
    n = alu.append(str(input('Nome: ')).strip().lower().title())
    n1 = nota.append(float(input('Nota 1: ')))
    n2 = nota.append(float(input('Nota 2: ')))
    alu.append(nota[:])
    p.append(alu[:])
    alu.clear()
    nota.clear()
    r = str(input('Deseja continuar? [S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('DIGITE CORRETAMENTE --Deseja continuar? [S/N]')).strip().upper()
    if r == 'N':
        break
print('==' * 50)
print('N.  NOME                MÉDIA                STATUS')
print('__' * 30)
for c in range(0, len(p)):
    m = (p[c][1][0] + p[c][1][1]) / 2
    print(f'{c}  {p[c][0]:<20} {m:<20} {"APROVADO" if m >= 60 else "REPROVADO"}')
s = 0
while True:
    print('__' * 30)
    h = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if h == 999:
        break
    print(f'As notas de {p[h][0]} são:  {p[h][1]}')

print('FINALIZANDO...')
sleep(0.5)
print('<<VOLTE SEMPRE>>')
