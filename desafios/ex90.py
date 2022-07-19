aluno = {}
n = aluno['nome'] = str(input('Nome: ')).lower().strip().title()
media = aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'O aluno {aluno["nome"]} está com média {aluno["media"]}',end='')
if aluno['media']>=70:
    print(' ... Situação: APROVADO',end=' ')
elif 50 < aluno['media'] < 70:
    print(' ...Situação: RECUPERAÇÃO',end=' ')
else:
    print(' ...Situação: REPROVADO', end=' ')