n1 = float((input('Digite a primeira nota: ')))
n2 = float((input('Digite a segunda nota: ')))
m = (n1 + n2) / 2
print(f'Sua média foi de {m:.1f}')

if m >= 60:
    print('Aluno aprovado')
else:
    print(f'Aluno reprovado por {60 - m} pontos')

#TE AMO MOR, ajeita tudinho pra se adequar aos seus estudos
