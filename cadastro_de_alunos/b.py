from time import sleep
from pacote import *


ar = 'alunos.txt'
if verifica(ar):
    print(f'{ar} encontrado com sucesso')
else:
    cria(ar)

while True:
    tit('CADASTRO DE PESSOAS')
    escolha(['Cadastrar nota e aluno','Ver alunos','Sair'])
    esc = num('Sua escolha: ')
    if esc ==1:
        while True:
            tit('CADASTRANDO NOVO ALUNO')
            temp = []
            nome = str(input('Nome do aluno: ')).strip().lower().title()
            nota1 = num('Nota 1: ')
            nota2 = num('Nota 2: ')
            media = (nota1+nota2)/2
            temp.append(nome)
            temp.append(nota1)
            temp.append(nota2)
            temp.append(media)
            escreve('alunos.txt',temp)
            temp.clear()
            es = sn('DESEJA CONTINUAR? [S/N]: ')
            if es =='S':
                sleep(1)
                continue
            else:
                sleep(1)
                break
    elif esc ==2:
        tit('ALUNOS CADASTRADOS')
        ler(ar)
        sleep(2)
    elif esc==3:
        break
