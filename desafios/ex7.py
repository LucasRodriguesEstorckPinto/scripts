n1= int(input('Digite sua nota na primeira prova:'))
n2= int(input('Digite sua nota na segunda prova:'))
m= (n1+n2)/2

print(f'Sua média é {m} pontos')

if m>=60:
    print('\033[1;31mALUNO APROVADO\033[m')
    
else:
    print('ALUNO REPROVADO')